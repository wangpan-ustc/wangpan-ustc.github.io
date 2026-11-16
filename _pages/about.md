---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

I am a Master's student in Electronic Information at the **University of Science and Technology of China (USTC)**. I received my B.Eng. in Electronic Information Engineering from **Hainan University**. From May to November 2026, I was a Research Intern at **Ant Group**, advised by [Yongqi Tong](https://scholar.google.co.jp/citations?user=y3iZyVcAAAAJ&hl=en) and [Wei Wu](https://scholar.google.co.jp/citations?hl=en&user=YtqXSzMAAAAJ).

My research focuses on **self-evolving LLM agents**, i.e., agents that keep improving from their own experience. Specifically, I work on:
- **Learning from experience without parameter updates**: reflection, skill memory, and credit assignment for agents ([REFLEX](https://arxiv.org/abs/2606.16496), NeurIPS 2026).
- **Failure diagnosis and recovery**: diagnosing why agents fail and repairing them selectively ([DARC](https://arxiv.org/abs/2608.11772), KDD 2027).
- **Agent skill acquisition at scale**: mining verifiable, reusable skills from code ([Code2Skill](https://arxiv.org/abs/2609.05571), Hugging Face Daily Papers #3).
- **Agent post-training**: SFT, preference optimization, and RL (DPO / GRPO) for multimodal agents.

I also have prior experience in computer vision, including image restoration and object detection.

More on my [Google Scholar](https://scholar.google.com/citations?user=rgx9sYAAAAAJ&hl=en).


# 🔥 News
<!-- TODO: 带 (?) 注释的月份是根据会议常规时间推测的，请核对后删除注释 -->
- *2026.11*: &nbsp;🎉🎉 Our paper **DARC** on selective self-correction for LLM agents is accepted to **KDD 2027**! <!-- (?) 月份待核对 -->
- *2026.10*: &nbsp;🔥 **PAR** ranked **#3** on [Hugging Face Daily Papers](https://huggingface.co/papers/2610.27628)!
- *2026.09*: &nbsp;🔥 **Code2Skill** ranked **#3** on [Hugging Face Daily Papers](https://huggingface.co/papers/2609.05571)!
- *2026.09*: &nbsp;🎉🎉 Our paper **REFLEX** on self-evolving agents is accepted to **NeurIPS 2026**! <!-- (?) 月份待核对 -->
- *2026.06*: &nbsp;🎉 **CogSENet** for blind image deblurring is accepted to **ECCV 2026**.
- *2026.05*: &nbsp;📄 **AtlasVA**, teacher-free visual skill memory for VLM agents, is released on [arXiv](https://arxiv.org/abs/2605.17933). Our [RedNote post](https://xhslink.cn/o/2bem1Afo25i) got **792** likes & stars!
- *2026.05*: &nbsp;💼 Joined **Ant Group** as a Research Intern.
- *2026.04*: &nbsp;🏆 Ranked **5th / 223** in the CVPR NTIRE 2026 Image Shadow Removal Challenge. <!-- (?) 月份待核对 -->


# 📝 Publications
<sup>*</sup> Equal contribution

## 2027

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2027</div><img src='images/darc.png' alt="DARC" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction](https://arxiv.org/abs/2608.11772)

**Pan Wang**, Yihao Hu, Hang Wang, Zirui Lv, Xin Zhang, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong

[**arXiv**](https://arxiv.org/abs/2608.11772) \| **CCF-A**
- A **diagnose-before-recover** paradigm (Profile → Diagnose → Evaluate → Distill → Freeze) that finds the dominant failure bottlenecks and triggers cost-aware self-correction only when the agent fails.
- Cuts average environment steps by **54.2%** and invalid actions by **92.9%** on ALFWorld. It also generalizes to AppWorld and XBRL Finance.
</div>
</div>

## 2026

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv</div><img src='images/par.png' alt="PAR" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking](https://arxiv.org/abs/2610.27628)

**Pan Wang**, Yihao Hu, Guangyuan Dong, Yitong Lin, Hang Wang, Zimi Liu, Zhihao Wen, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong

[**arXiv**](https://arxiv.org/abs/2610.27628) \| [**🤗 Hugging Face Daily Papers #3**](https://huggingface.co/papers/2610.27628)
- Makes extra recurrent depth in looped LMs useful for **longer problems**: iteration *k* is trained to match the state after the first *k* operations, and recurrent states are norm-anchored.
- On swap-S<sub>5</sub>, a Qwen2.5-0.5B model trained on ≤32 moves reaches **95.5%** full-state accuracy at 512 moves (**16×** the training length), versus 55.7% for RLT and 0.8% for explicit CoT.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv</div><img src='images/code2skill.png' alt="Code2Skill" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Code2Skill: Grounded Skill Synthesis from Code at Scale for Agentic Intelligence](https://arxiv.org/abs/2609.05571)

Yongqi Tong<sup>*</sup>, **Pan Wang**<sup>*</sup>, Hang Wang, Jianshe Li, Xin Zhang, Jiang-Ming Yang, Wei Wu

[**arXiv**](https://arxiv.org/abs/2609.05571) \| [**🤗 Hugging Face Daily Papers #3**](https://huggingface.co/papers/2609.05571)
- Builds **CodeSkillBank**: **1,006,822** validated skills mined from **19,769** GitHub repositories.
- Improves agents by **11.7%** on average across **72** protocol-matched experiments, covering 9 model configurations and 8 benchmarks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2026</div><img src='images/cogsenet.png' alt="CogSENet" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CogSENet: Blind Image Deblurring with Blur-Conditioned Semantic Routing and Explicit Frequency Fusion](https://arxiv.org/abs/2606.30030)

**Pan Wang**, Yihao Hu, Xiujin Liu

[**arXiv**](https://arxiv.org/abs/2606.30030) \| [**Springer**](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_13) \| **CCF-B**
- An eagle-vision-inspired deblurring network. A **Semantic-Driven State Space Module** regroups tokens by semantics through differentiable routing, and a **BiFreqFusionBlock** separates high- and low-frequency features with wavelets.
- A continuous **Blur Field** estimated from the blurry input is fused with CLIP semantic priors, so restoration adapts to spatially non-uniform blur.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2026</div><img src='images/reflex.png' alt="REFLEX" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[REFLEX: Reflective Evolution from LLM Experience](https://arxiv.org/abs/2606.16496)

**Pan Wang**

[**arXiv**](https://arxiv.org/abs/2606.16496) \| **CCF-A**
- A **training-free self-evolving agent** with a traceable Reflection–Generation–Memory–Credit Assignment loop. A vision-based Critic diagnoses failures, and a self-evolving **Skill Memory** accumulates, merges, and prunes reusable code skills.
- Under a 100-call budget, it solves Acrobot, Pendulum, and Lunar Lander in a median of **13 / 20 / 24** calls, about **half** the calls of the baselines. It also cuts the invalid-program rate from 14.7% to **0.6%**.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv</div><img src='images/atlasva.png' alt="AtlasVA" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents](https://arxiv.org/abs/2605.17933)

**Pan Wang**, Yihao Hu, Xiujin Liu, Jingchu Yang, Hang Wang, Zhihao Wen

[**arXiv**](https://arxiv.org/abs/2605.17933) \| [**Project Page**](https://wangpan-ustc.github.io/AtlasvaWeb) \| [**📕 RedNote (792 likes & stars)**](https://xhslink.cn/o/2bem1Afo25i)
- Keeps VLM-agent memory **visually grounded**: a teacher-free, three-layer visual skill memory (spatial heatmaps, visual exemplars, and symbolic text skills) that evolves from trajectory statistics without any external LLM supervision.
- Reuses self-evolving danger/affinity atlases as **dense shaping rewards** for RL. It outperforms text-centric memory baselines on Sokoban, FrozenLake, 3D embodied navigation, and 3D robotic manipulation.
</div>
</div>


## 2025

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">J. Agric. Food Res.</div><img src='images/multistrategy.jpg' alt="Multi-Strategy Framework" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A Multi-Strategy Framework for Enhancing Shatian Pomelo Detection in Real-World Orchards](https://doi.org/10.1016/j.jafr.2026.103277)

**Pan Wang**, Yihao Hu, Xiaodong Bai, Jingchu Yang, Leyi Zhou, Aiping Yang, Xiangxiang Li, Meiping Ding, Jianguo Yao

*Journal of Agriculture and Food Research* (JCR Q1, IF 7.2)

[**Paper**](https://doi.org/10.1016/j.jafr.2026.103277) \| [**arXiv**](https://arxiv.org/abs/2510.09948) \| [**Code**](https://github.com/Genk641/REAS-Det)
- A multi-strategy framework for real orchards, which tackles device-dependent tone shifts, unstable lighting, large scale variation, and occlusion. It builds the multi-scenario **STP-AgriData** dataset and the **REAS-Det** detector with GSV-Conv.
- Achieves **84.3% mAP@0.50** and 53.6% mAP@0.50:0.95 on STP-AgriData, outperforming recent detectors.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Smart Agric. Tech.</div><img src='images/sdedet.png' alt="SDE-DET" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SDE-DET: Precision Detection Network for Shatian Pomelos in Challenging Orchard Environments](https://doi.org/10.1016/j.atech.2026.101915)

Yihao Hu<sup>*</sup>, **Pan Wang**<sup>*</sup>, Xiaodong Bai, Shijie Cai, Hang Wang, Huazhong Liu, Aiping Yang, Xiangxiang Li, Meiping Ding, Hongyan Liu, Jianguo Yao

*Smart Agricultural Technology* (JCR Q1, IF 7.1)

[**Paper**](https://doi.org/10.1016/j.atech.2026.101915) \| [**arXiv**](https://arxiv.org/abs/2509.19990) \| [**Code**](https://github.com/yihaohu0118/SDE-DET)
- A pomelo detector for complex orchards that combines **Star Blocks**, **Deformable Attention** for occlusion, and **Efficient Multi-Scale Attention** for small objects.
- Reaches **0.838 mAP@0.5** (precision 0.883, F1 0.823), outperforming the YOLO series and other mainstream detectors.
</div>
</div>

## Patents
- An Interpretable Image-to-Text Description Method Based on Multi-Model Fusion, Invention Patent, CN202410750467.1, second inventor (supervisor listed first), **Granted**.


# 💻 Internships
- *2026.05 - 2026.11*, Research Intern, **Ant Group**, China. Advisors: [Yongqi Tong](https://scholar.google.co.jp/citations?user=y3iZyVcAAAAJ&hl=en) and [Wei Wu](https://scholar.google.co.jp/citations?hl=en&user=YtqXSzMAAAAJ).
  - **Million-scale agent skill synthesis**: Contributed to the fully automated **Code2Skill** pipeline, which mined and validated **1,006,822** executable skills from 19,000+ GitHub repositories.
  - **Failure diagnosis and repair for self-evolving agents**: Led **DARC**, which diagnoses why agents fail and distills cost-aware recovery policies, so that agents can repair themselves and keep evolving. Accepted to KDD 2027.
  - **Agent–environment co-evolution**: Contributed to **SEAL**, a framework in which agents and their learning environments evolve together, to support scalable agent RL.
  - **Multimodal agent post-training**: Implemented SFT, preference optimization, Offline-DPO, and GRPO for long-horizon visual reasoning and tool use.


# 🎖 Honors and Awards
- *2026* Excellence Award, UbiComp 2026 CUHK-X Multimodal Human Activity Challenge.
- *2026* **Rank 5 / 223**, CVPR NTIRE 2026 Image Shadow Removal Challenge.
- *2025* National Second Prize, China Robotics and Artificial Intelligence Competition.
- *2024* **National First Prize**, National College Student Digital Media Technology Works and Creativity Competition.
- *2024* National Second Prize, Global Campus Artificial Intelligence Algorithm Elite Competition.
- *2024* National Third Prize, National College Student Information Security Competition.
- *2024* National Third Prize, Lanqiao Cup National Software and Information Technology Competition.
- *2023* **National First Prize**, Global Campus Artificial Intelligence Algorithm Elite Competition.
- *2023 - 2025* National Undergraduate Innovation and Entrepreneurship Training Program: led 1 national-level project and participated in 2 others, all completed.


# 📖 Educations
- *2026 - now*, M.S. in Electronic Information, University of Science and Technology of China (USTC).
- *2022 - 2026*, B.Eng. in Electronic Information Engineering, Hainan University.
