---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Shenghe Zheng is an incoming Ph.D. student at The Hong Kong University of Science and Technology, supervised by [Prof. Jiaya Jia](https://jiaya.me). He received his Master’s degree from Harbin Institute of Technology in 2026, supervised by [Prof. Hongzhi Wang](http://homepage.hit.edu.cn/wang). Previously, Shenghe Zheng obtained his Bachelor’s degree from Harbin Institute of Technology in June 2023.

His current research interests lie in Large Language/Multimodal Models, Video Generation, and AI4Science. If you are seeking any form of academic cooperation, please feel free to email at [shenghez.zheng@gmail.com](shenghez.zheng@gmail.com).

# 📖 Educations
<div class="education-list">
  <div class="education-item">
    <div class="education-time">2023.08 - 2026.03</div>
    <div class="education-body">
      <strong>M.Sc. in Computer Science</strong>, Harbin Institute of Technology.
      <div class="education-note">Supervisor: Prof. Hongzhi Wang, Rank: 1/129.</div>
    </div>
  </div>
  <div class="education-item">
    <div class="education-time">2019.08 - 2023.06</div>
    <div class="education-body">
      <strong>B.Eng. in Computer Science</strong>, Harbin Institute of Technology.
    </div>
  </div>
</div>

# 🔥 News
<div class="news-list">
  <div class="news-item"><span class="news-date">2026.08</span><span class="news-content">🎉 One paper is accepted by EMNLP 2026 Findings.</span></div>
  <div class="news-item"><span class="news-date">2026.06</span><span class="news-content">🎉 Two papers are accepted by ECCV 2026.</span></div>
  <div class="news-item"><span class="news-date">2026.02</span><span class="news-content">🎉 Our <a href="https://arxiv.org/pdf/2511.21083">VIO</a>, FREE-Switch(Findings) are accepted by CVPR 2026.</span></div>
  <div class="news-item"><span class="news-date">2026.01</span><span class="news-content">🎉 Our <a href="https://arxiv.org/abs/2509.24285">SCI-Verifier</a> is accepted by ICLR 2026.</span></div>
  <div class="news-item"><span class="news-date">2025.09</span><span class="news-content">🎉 Our <a href="https://arxiv.org/abs/2506.00022">PHYSICS</a>, <a href="https://arxiv.org/abs/2506.06318">MoE-Gyro</a>, <a href="https://arxiv.org/abs/2505.13563">UltraDelta</a> are accepted by NeurIPS 2025.</span></div>
  <div class="news-item"><span class="news-date">2025.06</span><span class="news-content">🎉 Our <a href="https://arxiv.org/abs/2411.16815">FREE-Merging</a> is accepted by ICCV 2025.</span></div>
  <div class="news-item"><span class="news-date">2024.09</span><span class="news-content">🎉 Our <a href="https://arxiv.org/abs/2405.00957">IntraMix</a> is accepted by NeurIPS 2024.</span></div>
</div>

# 📝 Selected Publications 
† indicates equal contribution

<div class="publication-list" markdown="1">

## 🎯Large Language/Multimodal Models

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">ECCV 2026</span> <a href="https://arxiv.org/abs/2609.03729">Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning</a> Yijun Yang<sup>†</sup>, <strong>Shenghe Zheng<sup>†</sup></strong>, Wenbo Li, Jianhui Liu, Haoze Sun, Yanbing Zhang, Jiaxiu Jiang, Lin Song, Haoyang Huang, Nan Duan, Lei Zhu.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2609.03729" target="_blank" rel="noopener">PDF</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">ICLR 2026</span> <a href="https://arxiv.org/abs/2509.24285">SCI-Verifier: Scientific Verifier with Thinking</a> <strong>Shenghe Zheng<sup>†</sup></strong>, Chenyu Huang<sup>†</sup>, Fangchen Yu, Junchi Yao, Jingqi Ye, Tao Chen, Yun Luo, Ning Ding, Lei Bai, Ganqu Cui, Peng Ye.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2509.24285" target="_blank" rel="noopener">PDF</a><a class="publication-resource" href="https://github.com/Zhengsh123/SCI-Verifier" target="_blank" rel="noopener">Code</a><a class="publication-resource" href="https://huggingface.co/datasets/desimfj/SCI-VerifyBench" target="_blank" rel="noopener">Dataset</a><a class="publication-resource" href="https://huggingface.co/desimfj/SCI-Verifier-4B" target="_blank" rel="noopener">Model</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">NeurIPS 2025</span> <a href="https://arxiv.org/abs/2506.00022">Scaling Physical Reasoning with the PHYSICS Dataset</a> <strong>Shenghe Zheng<sup>†</sup></strong>, Qianjia Cheng<sup>†</sup>, Junchi Yao<sup>†</sup>, Mengsong Wu, Haonan He, Ning Ding, Yu Cheng, Shuyue Hu, Lei Bai, Dongzhan Zhou, Ganqu Cui, Peng Ye.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2506.00022" target="_blank" rel="noopener">PDF</a><a class="publication-resource" href="https://github.com/Zhengsh123/PHYSICS" target="_blank" rel="noopener">Code</a><a class="publication-resource" href="https://huggingface.co/datasets/desimfj/PHYSICS" target="_blank" rel="noopener">Dataset</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf tech-report">Tech Report</span> <a href="https://arxiv.org/abs/2511.13612">P1: Mastering Physics Olympiads with Reinforcement Learning</a> Jiacheng Chen, Qianjia Cheng, Fangchen Yu, Haiyuan Wan, Yuchen Zhang, <strong>Shenghe Zheng</strong>, Junchi Yao, Qingyang Zhang, Haonan He, Yun Luo, Yufeng Zhao, Futing Wang, Li Sheng, Chengxing Xie, Yuxin Zuo, Yizhuo Li, Wenxauan Zeng, Yulun Wu, Rui Huang, Dongzhan Zhou, Kai Chen, Yu Qiao, Lei Bai, Yu Cheng, Ning Ding, Bowen Zhou, Peng Ye, Ganqu Cui.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2511.13612" target="_blank" rel="noopener">PDF</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf tech-report">Tech Report</span> <a href="https://arxiv.org/abs/2602.09443">P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics Olympiads</a> Yun Luo, Futing Wang, Qianjia Cheng, Fangchen Yu, Haodi Lei, Jianhao Yan, Chenxi Li, Jiacheng Chen, Yufeng Zhao, Haiyuan Wan, Yuchen Zhang, <strong>Shenghe Zheng</strong>, Junchi Yao, Qingyang Zhang, Haonan He, Wenxuan Zeng, Li Sheng, Chengxing Xie, Yuxin Zuo, Yizhuo Li, Yulun Wu, Rui Huang, Dongzhan Zhou, Kai Chen, Yu Qiao, Lei Bai, Yu Cheng, Ning Ding, Bowen Zhou, Peng Ye, Ganqu Cui.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2602.09443" target="_blank" rel="noopener">PDF</a></div>
</article>

## 🎯Video Generation

<article class="publication-item">
  <p class="publication-main"><span class="conf arxiv">arXiv 2026</span> <a href="https://zhengsh123.github.io/V-Bridge/">V-Bridge: Bridging Video Generative Priors to Versatile Few-shot Image Restoration</a> <strong>Shenghe Zheng</strong>, Junpeng Jiang, Wenbo Li.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2603.13089" target="_blank" rel="noopener">PDF</a><a class="publication-resource" href="https://github.com/Zhengsh123/V-Bridge" target="_blank" rel="noopener">Code</a><a class="publication-resource" href="https://zhengsh123.github.io/V-Bridge/" target="_blank" rel="noopener">Website</a><a class="publication-resource" href="https://huggingface.co/desimfj/V-Bridge" target="_blank" rel="noopener">Model</a></div>
</article>

## 🎯Embodied AI

<article class="publication-item">
  <p class="publication-main"><span class="conf tech-report">Tech Report</span> <a href="https://arxiv.org/abs/2609.38059">WorldLine: Action-Driven Visual Simulation for Robotic Manipulation</a> <strong>Shenghe Zheng</strong>, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2609.38059" target="_blank" rel="noopener">PDF</a><a class="publication-resource" href="https://github.com/Zhengsh123/WorldLine" target="_blank" rel="noopener">Code</a><a class="publication-resource" href="https://zhengsh123.github.io/WorldLine/" target="_blank" rel="noopener">Website</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf tech-report">Tech Report</span> <a href="https://arxiv.org/abs/2609.00188">ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training</a> Xionghao Wu, Yijun Yang, Shiyang Zhou, Haoze Sun, Jianhui Liu, Songsong Yu, Jiyao Zhang, Wenbo Li, Bo Wang, Guoqing Ma, Lin Song, Renjie Liao, <strong>Shenghe Zheng</strong>, Wei Tang, Xiaojuan Qi, Yanwei Li, Yuan Zhang, Zhuotao Tian, Haoyang Huang, Nan Duan.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2609.00188" target="_blank" rel="noopener">PDF</a></div>
</article>


## 🎯Efficient AI

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">EMNLP 2026 (Findings)</span> <a href="https://arxiv.org/abs/2505.15875">Decouple and Orthogonalize: A Data-Free Framework for LoRA Merging</a> <strong>Shenghe Zheng</strong>, Hongzhi Wang, Chenyu Huang, Xiaohui Wang, Tao Chen, Jiayuan Fan, Shuyue Hu, Peng Ye.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2505.15875" target="_blank" rel="noopener">PDF</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">CVPR 2026 Findings</span> <a href="https://arxiv.org/abs/2604.10023">FREE-Switch: Frequency-based Dynamic LoRA Switch for Style Transfer</a> <strong>Shenghe Zheng</strong>, Minyu Zhang, Tianhao Liu, Hongzhi Wang.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2604.10023" target="_blank" rel="noopener">PDF</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">ICCV 2025</span> <a href="https://arxiv.org/abs/2411.16815">FREE-Merging: Fourier Transform for Model Merging with Lightweight Experts</a> <strong>Shenghe Zheng</strong>, Hongzhi Wang.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2411.16815" target="_blank" rel="noopener">PDF</a><a class="publication-resource" href="https://github.com/Zhengsh123/FREE-Merging" target="_blank" rel="noopener">Code</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">NeurIPS 2024</span> <a href="https://arxiv.org/abs/2405.00957">IntraMix: Intra-Class Mixup Generation for Accurate Labels and Neighbors</a> <strong>Shenghe Zheng</strong>, Hongzhi Wang, Xianglong Liu.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2405.00957" target="_blank" rel="noopener">PDF</a><a class="publication-resource" href="https://github.com/Zhengsh123/IntraMix" target="_blank" rel="noopener">Code</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">AAAI 2024</span> <a href="https://arxiv.org/abs/2302.13020">DCLP: Neural Architecture Predictor with Curriculum Contrastive Learning</a> <strong>Shenghe Zheng</strong>, Hongzhi Wang, Tianyu Mu.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2302.13020" target="_blank" rel="noopener">PDF</a><a class="publication-resource" href="https://github.com/Zhengsh123/DCLP" target="_blank" rel="noopener">Code</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">ICDE 2023</span> <a href="https://ieeexplore.ieee.org/document/9643158">AutoTSC: Optimization Algorithm to Automatically Solve the Time Series Classification Problem</a> Tianyu Mu, Hongzhi Wang, <strong>Shenghe Zheng</strong>.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://ieeexplore.ieee.org/document/9643158" target="_blank" rel="noopener">Paper</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">VLDB 2021</span> <a href="https://dl.acm.org/doi/10.14778/3476311.3476336">Assassin: an automatic classification system based on algorithm selection</a> Tianyu Mu, Hongzhi Wang, <strong>Shenghe Zheng</strong>.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://dl.acm.org/doi/10.14778/3476311.3476336" target="_blank" rel="noopener">Paper</a></div>
</article>


## 🎯AI4Science

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">CVPR 2026</span> <a href="https://arxiv.org/abs/2511.21083">Dual-Agent Reinforcement Learning for Adaptive and Cost-Aware Visual-Inertial Odometry</a> Feiyang Pan<sup>†</sup>, <strong>Shenghe Zheng<sup>†</sup></strong>, Chunyan Yin, Guangbin Dou.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2511.21083" target="_blank" rel="noopener">PDF</a></div>
</article>

<article class="publication-item">
  <p class="publication-main"><span class="conf accepted">NeurIPS 2025</span> <a href="https://arxiv.org/abs/2506.06318">MoE-Gyro: Self-Supervised Over-Range Reconstruction and Denoising for MEMS Gyroscopes</a> Feiyang Pan<sup>†</sup>, <strong>Shenghe Zheng<sup>†</sup></strong>, Chunyan Yin, Guangbin Dou.</p>
  <div class="publication-resources"><a class="publication-resource" href="https://arxiv.org/pdf/2506.06318" target="_blank" rel="noopener">PDF</a><a class="publication-resource" href="https://github.com/2002-Pan/Moe-Gyro" target="_blank" rel="noopener">Code</a></div>
</article>

</div>

# 🎖 Honors and Awards
<ul class="honor-list">
  <li><span>Outstanding Graduate of Heilongjiang Province</span><strong>2026</strong></li>
  <li><span>Outstanding Master’s Thesis of Harbin Institute of Technology</span><strong>2026</strong></li>
  <li><span>Outstanding Student of Heilongjiang Province</span><strong>2026</strong></li>
  <li><span>Outstanding Student Pacesetter of Harbin Institute of Technology</span><strong>2025</strong></li>
  <li><span>BYD Scholarship</span><strong>2025</strong></li>
  <li><span>Shengshengbuxi Scholarship</span><strong>2025</strong></li>
  <li><span>National Scholarship</span><strong>2024</strong></li>
  <li><span>Tencent Scholarship</span><strong>2024</strong></li>
  <li><span>Outstanding Graduate of Harbin Institute of Technology</span><strong>2023</strong></li>
  <li><span>Outstanding Student of Harbin Institute of Technology</span><strong>2019-2025</strong></li>
  <li><span>Renmin Scholarship</span><strong>2019-2022</strong></li>
</ul>

# Professional Activities
Reviewer: ICLR, NeurIPS, ICML, AAAI, TNNLS, ECAI
