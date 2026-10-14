from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublicationParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.publications = []
        self._current = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = set(attributes.get("class", "").split())
        if tag == "article" and "publication-item" in classes:
            self._current = {"statuses": [], "resources": []}
            self.publications.append(self._current)
        elif self._current is not None and tag == "span" and "conf" in classes:
            self._current["statuses"].append(classes)
        elif self._current is not None and tag == "a" and "publication-resource" in classes:
            self._current["resources"].append(attributes)

    def handle_endtag(self, tag):
        if tag == "article":
            self._current = None


def parse_publications():
    parser = PublicationParser()
    parser.feed((ROOT / "_pages" / "about.md").read_text())
    return parser.publications


class PublicationMarkupTest(unittest.TestCase):
    def test_every_publication_has_a_safe_official_resource_link(self):
        publications = parse_publications()

        self.assertEqual(17, len(publications))
        for publication in publications:
            self.assertTrue(publication["resources"])
            for resource in publication["resources"]:
                self.assertTrue(resource["href"].startswith("https://"))
                self.assertEqual("_blank", resource.get("target"))
                self.assertIn("noopener", resource.get("rel", "").split())

    def test_tech_reports_and_arxiv_use_distinct_status_classes(self):
        publications = parse_publications()
        status_classes = [classes for item in publications for classes in item["statuses"]]

        self.assertTrue(any("tech-report" in classes for classes in status_classes))
        self.assertTrue(any("arxiv" in classes for classes in status_classes))
        self.assertFalse(
            any("under-review" in classes for classes in status_classes),
            "Tech Report and arXiv should not share the legacy status class",
        )


if __name__ == "__main__":
    unittest.main()
