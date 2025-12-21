---
layout: default
title: Final Scientific Report
permalink: /final-report/
description: SNSF Final Scientific Report for Project 205487 - Network-Based Credit Risk Models in P2P Lending Markets
---

<div style="max-width:800px; margin:0 auto; font-size:0.95rem; line-height:1.6;">

**Final Scientific Report**

Network-Based Credit Risk Models in P2P Lending Markets

| | |
|---|---|
| Name | Prof. Dr. Joerg Osterrieder |
| Project number | 205487 |

---

**1.1 Achievement of research objectives (mandatory)**

**Main Objective:** To advance our understanding of credit risk modeling in P2P lending markets by designing and empirically verifying new network-based credit risk models. This project has attributes of a methodological and empirical project with practical impact, addressing information asymmetry inherent in P2P lending through network analysis.

**Contribution 1 (Methodological): Supervised Network-Based Credit Risk Models**

Previous methods (Ahelegbey et al., 2019; Giudici et al., 2019, 2020) ignored loan status, leading to unsupervised network-based learning. Our approach utilizes class information (loan default status) to construct supervised networks, as supervised learning generally outperforms unsupervised approaches. We developed a two-step machine learning methodology that constructs borrower similarity graphs and extracts multiple centrality measures (PageRank, betweenness, closeness, Katz, hub/authority) as predictive features.

Evidence: Liu et al. (2024), "Leveraging network topology for credit risk assessment in P2P lending," Expert Systems with Applications, Vol. 252, Article 124100. 17 citations.

**Contribution 2 (Methodological): Cross-Validation for Network Hyperparameters**

In contrast to previous studies, our work acknowledges that network creation and feature extraction depend on hyperparameters. We applied cross-validation to tune network hyperparameters and resulting features, including similarity thresholds, k-nearest-neighbor connection rules, and centrality measure configurations. This systematic approach to hyperparameter optimization contrasts with prior work that used fixed, ad-hoc parameter choices.

Evidence: Methods sections in Liu et al. (2024) ESWA and FRL publications; hyperparameter sensitivity analysis in Zenodo deposits.

**Contribution 3 (Methodological): Multiple Networks with Bootstrap Aggregation**

Previous studies created only one network. We designed methods to create multiple networks that: (i) utilize different (random) sets of variables, and (ii) rely on bootstrap aggregation (bagging). This directly addresses data noisiness, which is ignored in existing literature. The approach was validated using Elastic Net, Random Forest, Multi-Layer Perceptron, and XGBoost ensemble methods.

Evidence: Ensemble methodology in publications; robustness checks using shuffled centrality features confirmed predictive value.

**Contribution 4 (Empirical): Validation Across Multiple P2P Datasets**

We enriched the empirical literature (most studies use fewer than two datasets) by validating models across different market platforms. Primary analysis used the Bondora dataset (231,039 borrowers, 112 variables, European P2P market), with comparative validation using LendingClub data (US market). This enabled observation of credit drivers across platforms with different geographic and regulatory characteristics.

Evidence: Liu et al. (2024), "Network centrality and credit risk," Finance Research Letters, Vol. 63, Article 105308. 11 citations.

**Contribution 5 (Practical): Explainable AI for Interpretable Credit Risk Models**

We investigated the applicability of XAI methods (SHAP, LIME) to credit scoring models, enabling estimation of both global effects (expected effect of each variable on outcome) and local effects (expected effect of each variable for a specific individual loan). This addresses regulatory requirements for interpretable automated lending decisions (GDPR, policymaker trends). Surrogate decision trees and manual tree-based interpretation frameworks were developed for regime detection models.

Evidence: SHAP explainability notebooks in Zenodo deposit 17991107; tree-based interpretation framework in Zenodo deposit 17990398; 12 Zenodo deposits ensuring reproducibility.

**Additional Project Outcomes**

The project trained two PhD researchers (Lennart John Baals and Yiting Liu) who developed expertise in digital finance, network modeling, and explainable AI. We established collaborations with five international institutions across four continents (Masaryk University, Columbia University, American University of Sharjah, Renmin University of China, University of Manchester). The PI serves as Action Chair of COST Action CA19130 (Fintech and AI in Finance) and Coordinator of the MSCA Industrial Doctoral Network on Digital Finance.

Additional Funding Secured: The project's success attracted CHF 90,000 in additional funding: two SNSF Mobility Grants (CHF 20,000 each) and a Leading House Asia grant (CHF 50,000) for related digital assets research.

---

**1.2 Challenges, negative results and unexpected outcomes**

**Data Access Challenges:** The original proposal planned validation across 7 P2P platforms (Lending Club, Prosper, Zopa, Mintos, Bondora, Home Credit, Kiva). Due to data access restrictions, platform terms of service (e.g., Bondora section 13.4 preventing redistribution), and proprietary data policies, we focused primary empirical analysis on Bondora (European) with comparative validation using LendingClub (US), providing geographic and regulatory diversity. This led us to focus on reproducible code and documentation in our Zenodo deposits.

**Platform Evolution:** The P2P lending landscape evolved significantly during the project period, with some platforms reducing operations or changing data policies. Several planned data sources became unavailable or restricted. This required flexibility in our empirical strategy, ultimately strengthening our focus on methodological contributions applicable across different platforms.

**Computational Scaling:** Network construction for large loan portfolios presented computational challenges. We addressed this through efficient similarity thresholding and k-nearest-neighbor connection rules to maintain connectivity while managing graph size.

**Unexpected Finding:** Our analysis revealed that network position (degree centrality) alone provides substantial predictive power, sometimes matching or exceeding more complex centrality measures. This simplified insight has practical implications for platform operators seeking interpretable risk indicators.

---

**1.3 Contribution to knowledge advancement**

**Methodological Contribution:** We established network topology as a viable and valuable feature source for credit risk modeling in P2P lending. Our two-step ML approach provides a replicable framework for combining structural and attribute-based predictors. The systematic literature review (78 articles analyzed) provides a comprehensive synthesis of graph-based credit modeling approaches.

**Practical Impact:** Our models and code are directly applicable to P2P lending platforms for risk assessment. The interpretability framework using SHAP/LIME enables platform operators to explain credit decisions to borrowers and regulators, addressing transparency requirements in automated lending decisions.

**Open Science Contribution:** All 12 Zenodo deposits (100% open access) ensure complete reproducibility of our findings. The deposits include LaTeX sources, Jupyter notebooks, Python/R scripts, and comprehensive documentation, enabling other researchers to validate, extend, and build upon our work.

**Capacity Building:** Two PhD researchers were trained in cutting-edge methods at the intersection of network science, machine learning, and finance. Knowledge transfer activities included an Open Day workshop at FINMA (Swiss financial regulator) and presentations at international research events in eight countries.

**Research Network Leadership:** The PI's roles as COST Action Chair and MSCA Network Coordinator enabled broad dissemination of project findings across 40+ European institutions, creating lasting infrastructure for fintech research collaboration.

---

<details>
<summary><strong>Extended Project Information</strong></summary>

**Project Statistics:** 6+ Core Publications, 28+ Citations Received, 12 Zenodo Deposits, 8 Conference Presentations, 2 PhD Researchers Trained, CHF 90k Additional Funding.

**1.4 Impact Statement**

Scientific Impact: Our publications have received 28+ citations within 12 months of publication, indicating rapid adoption by the research community.

Economic Impact: The developed models and open-source code are directly applicable to P2P lending platforms for improved credit risk assessment.

Social Impact: Improved credit risk models contribute to financial inclusion by enabling P2P platforms to serve borrowers who may be underserved by traditional banking.

Policy Impact: The project engaged directly with financial regulators through the Open Day workshop (May 2024), presenting research findings to Swiss financial supervisory staff.

Educational Impact: The project trained 2 PhD researchers. The publication "Towards a new PhD Curriculum for Digital Finance" (Open Research Europe, 2024) disseminates best practices for doctoral training.

**1.5 Sustainability Plan**

Data Preservation: 12 Zenodo deposits archived with DOIs. Curated dataset archived at OSF. Code repositories maintained under Digital-AI-Finance organization on GitHub. All outputs under CC-BY 4.0.

**Appendix A: Peer-Reviewed Publications**

Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B. (2024). Leveraging network topology for credit risk assessment in P2P lending. Expert Systems with Applications, 252(B), 124100. DOI: 10.1016/j.eswa.2024.124100. 17 citations.

Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B. (2024). Network centrality and credit risk. Finance Research Letters, 63, 105308. DOI: 10.1016/j.frl.2024.105308. 11 citations.

Baumohl, E., Lyocsa, S., Vasanicova, P. (2024). Macroeconomic environment and the future performance of loans. International Review of Financial Analysis, 95, 103416.

Baals, L.J., Osterrieder, J., Hadji-Misheva, B., Liu, Y. (2024). Towards a new PhD Curriculum for Digital Finance. Open Research Europe, 4, 16513.

Submitted: Baals, L.J., et al. (2025). Network Evidence on Credit-Risk Pricing in P2P Lending. SSRN 5276337. Baals, L.J., et al. (2025). State-Dependent Pricing in FinTech Credit. SSRN 5421207.

**Appendix B: Open Science Deposits (Zenodo)**

{% for output in site.data.research_outputs %}
{{ output.title }}. {{ output.creators | join: ", " }} ({{ output.publication_date | slice: 0, 4 }}). {{ output.resource_type }}. [Zenodo]({{ output.zenodo_url }})
{% endfor %}

**Appendix C: Academic Events**

Dec 2024: 4th International Symposium on Big Data and AI, Hong Kong. Sep 2024: 8th Bern Conference on Fintech and AI in Finance. Sep 2024: AI Finance Insights, Istanbul. May 2024: COST FinAI Meets Istanbul. May 2024: Open Day Workshop, FINMA Campus, Bern. Dec 2023: 16th ERCIM Conference, Berlin. Sep 2023: 8th European COST Conference, Bern. Sep 2023: European Summer School in Financial Mathematics, Delft.

**Appendix D: Dataset**

Bondora P2P Lending Dataset. Coverage: June 2009 - April 2022. Sample: 231,039 borrowers, 112 variables. DOI: 10.21227/33kz-0s65. License: CC-BY 4.0.

**Appendix E: International Collaborations**

Masaryk University (Czech Republic), Columbia University (USA), American University of Sharjah (UAE), Renmin University of China (China), University of Manchester (UK).

**Appendix F: PhD Researchers**

Lennart John Baals - PhD In Progress, BFH/University of Twente, Graph-based credit models.
Yiting Liu - PhD In Progress, BFH/University of Twente, P2P lending risk modeling.

</details>

---

Report submitted to: Swiss National Science Foundation (SNSF). Report date: December 2025. Data source: [SNSF Data Portal - Grant 205487](https://data.snf.ch/grants/grant/205487)

</div>
