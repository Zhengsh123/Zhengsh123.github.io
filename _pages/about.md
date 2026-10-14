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

<span class="conf accepted">ECCV 2026</span> [Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning](https://arxiv.org/pdf/2609.03729) Yijun Yang<sup>†</sup>, **Shenghe Zheng<sup>†</sup>**, Wenbo Li, Jianhui Liu, Haoze Sun, Yanbing Zhang, Jiaxiu Jiang, Lin Song, Haoyang Huang, Nan Duan, Lei Zhu.


<span class="conf accepted">ICLR 2026</span> [SCI-Verifier: Scientific Verifier with Thinking](https://arxiv.org/abs/2509.24285) **Shenghe Zheng<sup>†</sup>**, Chenyu Huang<sup>†</sup>, Fangchen Yu, Junchi Yao, Jingqi Ye, Tao Chen, Yun Luo, Ning Ding, Lei Bai, Ganqu Cui, Peng Ye.

<span class="conf accepted">NeurIPS 2025</span> [Scaling Physical Reasoning with the PHYSICS Dataset](https://arxiv.org/abs/2506.00022) **Shenghe Zheng<sup>†</sup>**, Qianjia Cheng<sup>†</sup>, Junchi Yao<sup>†</sup>, Mengsong Wu, Haonan He, Ning Ding, Yu Cheng, Shuyue Hu, Lei Bai, Dongzhan Zhou, Ganqu Cui, Peng Ye.

<span class="conf under-review">Tech Report</span> [P1: Mastering Physics Olympiads with Reinforcement Learning](https://arxiv.org/abs/2511.13612) Jiacheng Chen, Qianjia Cheng, Fangchen Yu, Haiyuan Wan, Yuchen Zhang, **Shenghe Zheng**, Junchi Yao, Qingyang Zhang, Haonan He, Yun Luo, Yufeng Zhao, Futing Wang, Li Sheng, Chengxing Xie, Yuxin Zuo, Yizhuo Li, Wenxauan Zeng, Yulun Wu, Rui Huang, Dongzhan Zhou, Kai Chen, Yu Qiao, Lei Bai, Yu Cheng, Ning Ding, Bowen Zhou, Peng Ye, Ganqu Cui.

<span class="conf under-review">Tech Report</span> [P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics Olympiads](https://arxiv.org/pdf/2602.09443) Yun Luo, Futing Wang, Qianjia Cheng, Fangchen Yu, Haodi Lei, Jianhao Yan, Chenxi Li, Jiacheng Chen, Yufeng Zhao, Haiyuan Wan, Yuchen Zhang, **Shenghe Zheng**, Junchi Yao, Qingyang Zhang, Haonan He, Wenxuan Zeng, Li Sheng, Chengxing Xie, Yuxin Zuo, Yizhuo Li, Yulun Wu, Rui Huang, Dongzhan Zhou, Kai Chen, Yu Qiao, Lei Bai, Yu Cheng, Ning Ding, Bowen Zhou, Peng Ye, Ganqu Cui.

## 🎯Video Generation

<span class="conf under-review">Arxiv 2026</span> [V-Bridge: Bridging Video Generative Priors to Versatile Few-shot Image Restoration](https://zhengsh123.github.io/V-Bridge/) **Shenghe Zheng**, Junpeng Jiang, Wenbo Li.

## 🎯Embodied AI

<span class="conf under-review">Tech Report</span> [WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](https://arxiv.org/abs/2609.38059) **Shenghe Zheng**, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia.

<span class="conf under-review">Tech Report</span> [ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training](https://arxiv.org/abs/2609.00188) Xionghao Wu, Yijun Yang, Shiyang Zhou, Haoze Sun, Jianhui Liu, Songsong Yu, Jiyao Zhang, Wenbo Li, Bo Wang, Guoqing Ma, Lin Song, Renjie Liao, **Shenghe Zheng**, Wei Tang, Xiaojuan Qi, Yanwei Li, Yuan Zhang, Zhuotao Tian, Haoyang Huang, Nan Duan.


## 🎯Efficient AI

<span class="conf accepted">EMNLP 2026(Findings)</span> [Decouple and Orthogonalize: A Data-Free Framework for LoRA Merging](https://arxiv.org/abs/2505.15875) **Shenghe Zheng**, Hongzhi Wang, Chenyu Huang, Xiaohui Wang, Tao Chen, Jiayuan Fan, Shuyue Hu, Peng Ye.

<span class="conf accepted">CVPR 2026 findings</span> [FREE-Switch: Frequency-based Dynamic LoRA Switch for Style Transfer](https://arxiv.org/abs/2604.10023) **Shenghe Zheng**, Minyu Zhang, Tianhao Liu, Hongzhi Wang.

<span class="conf accepted">ICCV 2025</span> [FREE-Merging: Fourier Transform for Model Merging with Lightweight Experts](https://arxiv.org/abs/2411.16815) **Shenghe Zheng**, Hongzhi Wang.

<span class="conf accepted">NeurIPS 2024</span> [IntraMix: Intra-Class Mixup Generation for Accurate Labels and Neighbors](https://arxiv.org/abs/2405.00957) **Shenghe Zheng**, Hongzhi Wang, Xianglong Liu.

<span class="conf accepted">AAAI 2024</span> [DCLP: Neural Architecture Predictor with Curriculum Contrastive Learning](https://arxiv.org/abs/2302.13020) **Shenghe Zheng**, Hongzhi Wang, Tianyu Mu.

<span class="conf accepted">ICDE 2023</span> [AutoTSC: Optimization Algorithm to Automatically Solve the Time Series Classification Problem](https://ieeexplore.ieee.org/document/9643158) Tianyu Mu, Hongzhi Wang, **Shenghe Zheng**.

<span class="conf accepted">VLDB 2021</span> [Assassin: an automatic classification system based on algorithm selection](https://dl.acm.org/doi/abs/10.14778/3476311.3476336) Tianyu Mu, Hongzhi Wang, **Shenghe Zheng**.


## 🎯AI4Science

<span class="conf accepted">CVPR 2026</span> [Dual-Agent Reinforcement Learning for Adaptive and Cost-Aware Visual-Inertial Odometry](https://arxiv.org/pdf/2511.21083) Feiyang Pan<sup>†</sup>, **Shenghe Zheng<sup>†</sup>**, Chunyan Yin, Guangbin Dou

<span class="conf accepted">NeurIPS 2025</span> [MoE-Gyro: Self-Supervised Over-Range Reconstruction and Denoising for MEMS Gyroscopes](https://arxiv.org/abs/2506.06318) Feiyang Pan<sup>†</sup>, **Shenghe Zheng<sup>†</sup>**, Chunyan Yin, Guangbin Dou

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
