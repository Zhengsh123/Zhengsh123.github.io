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

Shenghe Zheng is a second-year master degree candidate at the Department of Computer Science, Harbin Institute of Technology, fortunately advised by [Prof.Hongzhi Wang]( http://homepage.hit.edu.cn/wang). Previously, Shenghe Zheng obtained his Bachelor’s degree from Harbin Institute of Technology in June 2023.

His current research interests lie in Large Language Models, Multimodal Models, Efficient AI, and Neural Architecture Search(NAS). Currently, he is interning at the Shanghai AI Lab, conducting research related to large language models under the guidance of Dr. Peng Ye, and collaborating closely with [Dr. Ganqu Cui](https://cgq15.github.io/). If you are seeking any form of academic cooperation, please feel free to email at [shenghez.zheng@gmail.com](shenghez.zheng@gmail.com).

# 📖 Educations
- *2023.08 - now*, Master Candidate in Computer Science, **Harbin Institute of Technology**.
  - Supervisor: Prof. Hongzhi wang, Rank: 1/129.
- *2019.08 - 2023.06*, B.Eng. in Computer Science, **Harbin Institute of Technology**.

# 🔥 News
- *2025.09*: 🎉 Our [PHYSICS](https://arxiv.org/abs/2506.00022), [MoE-Gyro](https://arxiv.org/abs/2506.06318), [UltraDelta](https://arxiv.org/abs/2505.13563) are accepted by NeurIPS 2025.
- *2025.06*: 🎉 Our [FREE-Merging](https://arxiv.org/abs/2411.16815) is accepted by ICCV 2025.
- *2024.09*: 🎉 Our [IntraMix](https://arxiv.org/abs/2405.00957) is accepted by NeurIPS 2024.

# 📝 Selected Publications 
† indicates equal contribution

## 🎯Post-training
NeurIPS 2025 [Scaling Physical Reasoning with the PHYSICS Dataset](https://arxiv.org/abs/2506.00022) **Shenghe Zheng<sup>†</sup>**, Qianjia Cheng<sup>†</sup>, Junchi Yao<sup>†</sup>, Mengsong Wu, Haonan He, Ning Ding, Yu Cheng, Shuyue Hu, Lei Bai, Dongzhan Zhou, Ganqu Cui, Peng Ye

## 🎯Efficient AI


## 🎯AI4Science

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/MoE-Gyro.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MoE-Gyro: Self-Supervised Over-Range Reconstruction and Denoising for MEMS Gyroscopes](https://arxiv.org/abs/2506.06318)

Feiyang Pan<sup>†</sup>, **Shenghe Zheng<sup>†</sup>**, Chunyan Yin, Guangbin Dou

-  To address the issue of low noise performance and limited range in low-cost gyroscopes, we propose a generative approach for noise reduction and peak compensation. Additionally, due to the lack of data in this domain, we constructed a targeted dataset.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/FREE-Merging.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FREE-Merging: Fourier Transform for Model Merging with Lightweight Experts](https://arxiv.org/abs/2411.16815)

**Shenghe Zheng**, Hongzhi Wang. [**Code**](https://github.com/Zhengsh123/FREE-Merging)

-  We find that task-specific information from fine-tuning harms Model Merging, so we use frequency-domain filtering to reduce conflicts and utilize lightweight experts to compensate for information loss during model merging.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/IntraMix.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[IntraMix: Intra-Class Mixup Generation for Accurate Labels and Neighbors](https://arxiv.org/abs/2405.00957)

**Shenghe Zheng**, Hongzhi Wang, Xianglong Liu. [**Code**](https://github.com/Zhengsh123/IntraMix)

- This paper introduces IntraMix, seamlessly applying Mixup to graph augmentation, enhancing model effectiveness in data-scarce scenarios.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2024</div><img src='images/DCLP.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DCLP: Neural Architecture Predictor with Curriculum Contrastive Learning](https://arxiv.org/abs/2302.13020)

**Shenghe Zheng**, Hongzhi Wang, Tianyu Mu. [**Code**](https://github.com/Zhengsh123/DCLP)

- This paper introduces contrastive and curriculum learning for neural predictors, greatly reducing the performance evaluation cost in NAS.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICDE 2023</div><img src='images/TSC_AutoML.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AutoTSC: Optimization Algorithm to Automatically Solve the Time Series Classification Problem](https://ieeexplore.ieee.org/document/9643158)

Tianyu Mu, Hongzhi Wang, **Shenghe Zheng** 

- 
This paper introduces AutoML to time series classification, using dataset similarity to recommend algorithms for new datasets automatically.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">VLDB 2021</div><img src='images/Assassin.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Assassin: an automatic classification system based on algorithm selection](https://dl.acm.org/doi/abs/10.14778/3476311.3476336)

Tianyu Mu, Hongzhi Wang, **Shenghe Zheng** 

- This paper uses reinforcement learning to select meta-features and recommend algorithms with hyperparameters for new datasets automatically.
</div>
</div>

# 📝 Preprint 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2025</div><img src='images/DO-Merging.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Decouple and Orthogonalize: A Data-Free Framework for LoRA Merging](https://arxiv.org/abs/2505.15875)

**Shenghe Zheng**, Hongzhi Wang, Chenyu Huang, Xiaohui Wang, Tao Chen, Jiayuan Fan, Shuyue Hu, Peng Ye

-  We find that existing model merging methods are ineffective for LoRA due to large parameter magnitude differences. We propose a decoupling approach and optimize it via data-free orthogonalization.
</div>
</div>

# 🎖 Honors and Awards
- National Scholarship, *2024*
- Tencent Scholarship, *2024*
- Outstanding Graduate of Harbin Institute of Technology, *2023*
- Second Prize at the 14th Undergraduate Academic Forum, Harbin Institute of Technology, *2021*
- Honorable Award in American Mathematics Modelling Contest for College Students, *2021*
- Outstanding Student of Harbin Institute of Technology, *2019-2024*
- Renmin Scholarship, *2019-2022*

# Professional Activities
Reviewer: NeurIPS2025, ECAI2025

