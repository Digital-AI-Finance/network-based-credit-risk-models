---
layout: default
title: Final Scientific Report
permalink: /final-report/
description: SNSF Final Scientific Report for Project 205487 - Network-Based Credit Risk Models in P2P Lending Markets
---

<style>
.report-content { max-width: 800px; margin: 0 auto; font-size: 0.95rem; line-height: 1.6; }
.report-content h1 { text-align: center; margin-bottom: 0.5rem; }
.report-content h2 { margin-top: 2rem; border-bottom: 2px solid #c5a028; padding-bottom: 0.3rem; }
.report-content h3 { margin-top: 1.5rem; }
.report-content table { margin: 1rem auto; }
.report-content hr { margin: 2rem 0; }
.download-btn { display: inline-block; background: #1e3a5f; color: white; padding: 0.5rem 1rem; border-radius: 4px; text-decoration: none; margin: 1rem 0; }
.download-btn:hover { background: #2d4a7c; color: white; }
.download-container { text-align: center; margin: 1rem 0; }
</style>

<div class="report-content" markdown="1">

# Final Scientific Report

Network-Based Credit Risk Models in P2P Lending Markets

<div class="download-container">
<a href="{{ site.baseurl }}/assets/downloads/SNSF_Report_205487.docx" class="download-btn">Download Word Document (.docx)</a>
</div>

| | |
|---|---|
| Name | Prof. Dr. Joerg Osterrieder |
| Project number | 205487 |

---

## 1.1 Achievement of research objectives (mandatory)

**Main Objective:** To advance our understanding of credit risk modeling in P2P lending markets by designing and empirically verifying new network-based credit risk models. This project has attributes of a methodological and empirical project with practical impact, addressing information asymmetry inherent in P2P lending through network analysis. The main objective has been fully achieved through five distinct contributions that delivered novel methodology, rigorous empirical validation, and practical tools for interpretable credit risk assessment.

### Contribution 1 (Methodological): Supervised Network-Based Credit Risk Models

Previous methods in the literature (Ahelegbey et al., 2019; Giudici et al., 2019, 2020) ignored loan status when constructing borrower networks, leading to unsupervised network-based learning approaches. Our approach fundamentally differs by utilizing class information (loan default status) to construct supervised networks, recognizing that supervised learning algorithms generally outperform unsupervised approaches for prediction tasks. We developed a two-step machine learning methodology that first constructs borrower similarity graphs using mixed-type distance measures (Gower distance for handling both continuous and categorical borrower attributes) and then extracts multiple network centrality measures as predictive features. The centrality measures include PageRank, betweenness centrality, closeness centrality, Katz centrality, and hub/authority scores, each capturing different aspects of a borrower's position within the similarity network. Graph construction employed k-nearest-neighbor connection rules combined with similarity threshold-based edge selection to ensure network connectivity while maintaining meaningful structure. This contribution has been fully achieved. Evidence: Liu et al. (2024), "Leveraging network topology for credit risk assessment in P2P lending: A comparative study under the lens of machine learning," Expert Systems with Applications, Vol. 252, Article 124100 (DOI: 10.1016/j.eswa.2024.124100), with 17 citations in Scopus demonstrating rapid adoption by the research community.

### Contribution 2 (Methodological): Cross-Validation for Network Hyperparameters

In contrast to previous studies that used fixed, ad-hoc parameter choices, our work explicitly acknowledges that network creation and feature extraction depend on a set of hyperparameters whose optimal values vary depending on the specific dataset and network construction approach. We implemented systematic cross-validation to tune network hyperparameters and resulting features. The hyperparameter search space included similarity thresholds ranging from 0.1 to 0.9, k values for k-nearest-neighbor graphs ranging from 5 to 50, and different configurations of centrality measure computation. We employed 5-fold cross-validation throughout the model development process to ensure that hyperparameter selection was not overfit to a specific data split. This systematic approach to hyperparameter optimization represents a methodological advance over prior work and ensures reproducibility across different P2P lending contexts. This contribution has been fully achieved. Evidence: Methods sections in Liu et al. (2024) Expert Systems with Applications and Finance Research Letters publications document the complete hyperparameter tuning methodology; Zenodo deposits provide code for reproducible hyperparameter sensitivity analysis.

### Contribution 3 (Methodological): Multiple Networks with Bootstrap Aggregation

Previous studies in the literature created only one network representation. We designed methods to create multiple networks that differ in two key aspects: (i) they utilize different random subsets of variables for similarity computation, and (ii) they rely on bootstrap aggregation (bagging) to combine predictions from models trained on different network representations. This approach directly addresses data noisiness, which is ignored in the existing literature on network-based credit scoring. The ensemble methodology was validated using four machine learning models: Elastic Net regression, Random Forest, Multi-Layer Perceptron (MLP) neural networks, and XGBoost gradient boosting. To verify that network features contain genuine predictive signal rather than spurious correlations, we conducted robustness checks using shuffled centrality features where network positions were randomly permuted across borrowers. When centrality features were shuffled, predictive power dropped substantially, confirming that the network topology captures genuine information about default risk rather than acting as a proxy for other features. This contribution has been fully achieved. Evidence: Ensemble methodology and robustness validation results are documented in the published papers and reproducible through Zenodo deposit 17991107.

### Contribution 4 (Empirical): Validation Across Multiple P2P Datasets

We enriched the empirical literature, where most studies have used fewer than two P2P market datasets, by validating our models across different market platforms to observe credit drivers and method usefulness across diverse contexts. Primary empirical analysis used the Bondora dataset, a leading European P2P lending platform, containing 231,039 individual borrowers characterized through 112 categorical and continuous variables, with loan origination dates spanning from June 16, 2009 to April 21, 2022. The dataset includes detailed borrower demographics, financial attributes, and past credit market interactions. Comparative validation using LendingClub data from the United States market confirmed cross-market validity of our methodology. This geographic and regulatory diversity (European vs. US markets) strengthens the generalizability of our findings. A notable empirical finding was that degree centrality alone provides substantial predictive power for default risk, sometimes matching or exceeding more complex centrality measures like PageRank or betweenness centrality, suggesting that simpler network metrics may suffice for practical credit risk applications. This contribution has been fully achieved. Evidence: Liu et al. (2024), "Network centrality and credit risk: A comprehensive analysis of peer-to-peer lending dynamics," Finance Research Letters, Vol. 63, Article 105308 (DOI: 10.1016/j.frl.2024.105308), with 11 citations.

### Contribution 5 (Practical): Explainable AI for Interpretable Credit Risk Models

We investigated the applicability of existing XAI methods to credit scoring models, enabling the development of interpretable credit risk models that address regulatory requirements for explainable automated lending decisions. SHAP (SHapley Additive exPlanations) values were computed for all features including network centrality measures, providing both global feature importance (expected effect of each variable on the outcome across all loans) and local explanations (expected effect of each variable for a specific individual loan application). LIME (Local Interpretable Model-agnostic Explanations) was implemented for complementary local interpretability. Beyond standard XAI techniques, we developed surrogate decision trees for regime detection model interpretability and a manual tree-based interpretation framework for understanding macro-regime classification in credit markets. These interpretability tools address the regulatory requirements emphasized by policymakers concerning automatized lending solutions, including GDPR requirements for explanation of automated decisions. This contribution has been fully achieved. Evidence: SHAP explainability notebooks in Zenodo deposit 17991107 (journal article reproducibility); tree-based interpretation framework in Zenodo deposit 17990398 (state-dependent pricing interpretability); all 12 Zenodo deposits ensure complete reproducibility of interpretability analyses.

### Additional Project Outcomes

The project trained two PhD researchers, Lennart John Baals and Yiting Liu, who developed expertise in digital finance, network modeling, machine learning, and explainable AI. Both researchers are progressing toward completion of their doctoral theses at the University of Twente in collaboration with Bern University of Applied Sciences. We established substantive research collaborations with five international institutions across four continents: Masaryk University (Czech Republic) for joint publications and in-depth methodological exchanges; Columbia University (USA) for method exchanges and personnel exchange visits; American University of Sharjah (UAE) for joint publications and personnel exchange; Renmin University of China (China) for method exchanges and collaborative publications; and University of Manchester (UK) for joint publications. The PI serves as Action Chair of COST Action CA19130 (Fintech and AI in Finance), coordinating research collaboration across 40+ European institutions, and as Coordinator of the MSCA Industrial Doctoral Network on Digital Finance. Additional funding secured totaling CHF 90,000 includes two SNSF Mobility Grants (CHF 20,000 each) supporting researcher exchanges and a Leading House Asia grant (CHF 50,000) for related digital assets research.

---

## 1.2 Challenges, negative results and unexpected outcomes

**Data Access Challenges:** The original proposal planned validation across seven P2P platforms: Lending Club, Prosper, Zopa, Mintos, Bondora, Home Credit, and Kiva. Due to evolving data access restrictions, platform terms of service, and proprietary data policies, the scope of empirical validation was refined during project execution. Bondora's terms of service (Section 13.4) prevent redistribution of downloaded data, limiting our ability to share raw datasets while maintaining compliance. Similar restrictions applied to other planned platforms. We therefore focused primary empirical analysis on Bondora (European market) with comparative validation using LendingClub (US market), providing both geographic and regulatory diversity. This constraint led us to emphasize reproducible code and comprehensive documentation in our Zenodo deposits, ensuring that researchers with legitimate data access can replicate our methodology.

**Platform Evolution:** The P2P lending landscape evolved significantly during the project period (October 2022 - August 2025). Several platforms reduced operations, changed business models, or implemented more restrictive data access policies. The global rise in interest rates during 2022-2023 affected P2P lending volumes and platform viability across markets. This required flexibility in our empirical strategy, ultimately strengthening our focus on methodological contributions that remain applicable across different platforms regardless of specific data availability.

**Computational Scaling:** Network construction for large loan portfolios presented computational challenges. Building similarity graphs for 231,039 borrowers requires efficient algorithms to avoid quadratic complexity in pairwise distance computation. We addressed this through efficient similarity thresholding (computing distances only for potentially connected pairs) and k-nearest-neighbor connection rules that maintain network connectivity while managing computational load. These algorithmic choices are documented in our code repositories for researchers facing similar scaling challenges.

**Unexpected Finding:** Our empirical analysis revealed that network position measured by simple degree centrality alone provides substantial predictive power for default risk, sometimes matching or exceeding more computationally expensive centrality measures such as PageRank, betweenness, or Katz centrality. This finding has practical implications for platform operators seeking interpretable and computationally efficient risk indicators. The simplicity of degree centrality (counting direct connections) makes it easier to explain to stakeholders and regulators compared to more complex network metrics, supporting adoption of network-based credit assessment in practice.

---

## 1.3 Contribution to knowledge advancement

**Methodological Contribution:** We established network topology as a viable and valuable feature source for credit risk modeling in P2P lending, demonstrating that borrower position within similarity-based networks contains predictive information about default risk beyond what is captured by traditional borrower-level attributes alone. Our two-step machine learning approach (network construction followed by centrality-based feature extraction) provides a replicable framework for combining structural and attribute-based predictors. The systematic literature review conducted as part of this project analyzed 78 articles selected from 1,066 initially retrieved records through structured screening in Scopus and Web of Science, employing double-blind coding to ensure consistency. This review provides a comprehensive synthesis of graph-based credit modeling approaches across P2P lending and banking network applications, identifying research gaps and methodological best practices.

**Practical Impact:** Our models and code are directly applicable to P2P lending platforms for credit risk assessment. The interpretability framework using SHAP and LIME enables platform operators to explain credit decisions to borrowers and regulators, addressing transparency requirements in automated lending decisions mandated by regulations including GDPR. The finding that simple degree centrality provides substantial predictive power offers practitioners an accessible entry point to network-based credit modeling without requiring expertise in complex network science methods.

**Open Science Contribution:** All 12 Zenodo deposits are 100% open access, ensuring complete reproducibility of our findings. The deposits include LaTeX manuscript sources, Jupyter notebooks implementing the complete analysis pipeline from data preprocessing through model training and evaluation, Python and R scripts for network construction and centrality computation, and comprehensive documentation enabling other researchers to validate, extend, and build upon our work. The curated Bondora dataset is archived at the Open Science Framework (OSF) at https://osf.io/jnpfs/.

**Capacity Building:** Two PhD researchers were trained in cutting-edge methods at the intersection of network science, machine learning, and finance, developing skills directly relevant to the growing fintech sector. Knowledge transfer activities included presentations at international research events in eight countries: Switzerland, Germany, Turkey, Netherlands, Hong Kong, China, Czech Republic, and UAE.

**Research Network Leadership:** The PI's roles as COST Action CA19130 Chair and MSCA Digital Finance Network Coordinator enabled broad dissemination of project findings across 40+ European institutions, creating lasting infrastructure for fintech research collaboration that extends well beyond this individual project. The COST Action facilitated policy discussions at EU level including events in Brussels addressing AI in finance implications for financial regulation.

---

## Extended Project Information

**Project Statistics:** Eight core publications with 28+ total citations received, 12 Zenodo deposits ensuring reproducibility, 12 conference presentations across 8 countries, 2 PhD researchers trained, and CHF 90,000 in additional funding secured.

### 1.4 Impact Statement

**Scientific Impact:** Our publications have received 28+ citations within 12 months of publication, indicating rapid adoption by the research community. The two-step machine learning methodology combining network centrality with traditional credit features has been referenced in subsequent studies on P2P lending risk assessment, and the systematic literature review provides a foundational reference for researchers entering the field of graph-based credit modeling.

**Economic Impact:** The developed models and open-source code are directly applicable to P2P lending platforms for improved credit risk assessment. By enabling more accurate default prediction, platforms can better price loans to reflect true risk, reduce losses from defaults, and offer more competitive rates to creditworthy borrowers. The interpretability framework addresses regulatory requirements, reducing compliance costs for platforms adopting automated credit decisions.

**Social Impact:** Improved credit risk models contribute to financial inclusion by enabling P2P platforms to serve borrowers who may be underserved by traditional banking. More accurate risk assessment reduces adverse selection problems, protecting retail investors who fund P2P loans from excessive default losses. The transparency framework enhances borrower trust in automated credit decisions by providing explanations for lending outcomes.

**Policy Impact:** The PI's leadership of COST Action CA19130 facilitated policy discussions at EU level, including events in Brussels addressing AI in finance policy implications and contributing to the broader discourse on responsible AI adoption in financial services.

**Educational Impact:** The project trained two PhD researchers in cutting-edge methods at the intersection of network science, machine learning, and finance. The publication "Towards a new PhD Curriculum for Digital Finance" (Open Research Europe, 2024, DOI: 10.12688/openreseurope.16513.1) disseminates best practices for doctoral training in this emerging field, contributing to curriculum development beyond this specific project.

### 1.5 Sustainability Plan

**Data Preservation:** Twelve Zenodo deposits are archived with persistent DOIs ensuring permanent accessibility and citability through CERN's infrastructure. The curated Bondora P2P lending dataset is archived at the Open Science Framework (OSF). Code repositories are maintained under the Digital-AI-Finance organization on GitHub. All outputs are released under Creative Commons Attribution 4.0 (CC-BY 4.0) licensing, enabling unrestricted reuse with attribution.

**Code Maintainability:** All Jupyter notebooks and Python/R scripts include dependency specifications (requirements.txt, environment files) enabling reproduction with specified package versions. Reproducibility has been verified through independent testing. Documentation is embedded in code through comments and supplementary README files.

**Knowledge Transfer Continuation:** COST Action CA19130 (Fintech and AI in Finance) continues beyond project end with the PI serving as Action Chair. The MSCA Industrial Doctoral Network on Digital Finance continues training next-generation researchers with the PI as Coordinator. Digital finance research continues at Bern University of Applied Sciences building on this project's foundations.

### Appendix A: Peer-Reviewed Publications

Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B. (2024). Leveraging network topology for credit risk assessment in P2P lending: A comparative study under the lens of machine learning. Expert Systems with Applications, 252(B), 124100. DOI: 10.1016/j.eswa.2024.124100. 17 citations.

Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B. (2024). Network centrality and credit risk: A comprehensive analysis of peer-to-peer lending dynamics. Finance Research Letters, 63, 105308. DOI: 10.1016/j.frl.2024.105308. 11 citations.

Baumohl, E., Lyocsa, S., Vasanicova, P. (2024). Macroeconomic environment and the future performance of loans: Evidence from three peer-to-peer platforms. International Review of Financial Analysis, 95, 103416. DOI: 10.1016/j.irfa.2024.103416.

Baals, L.J., Osterrieder, J., Hadji-Misheva, B., Liu, Y. (2024). Towards a new PhD Curriculum for Digital Finance. Open Research Europe, 4, 16513. DOI: 10.12688/openreseurope.16513.1.

Lyocsa, S., Todorovic, N., Baals, L.J., Gao, H. (2025). Alpha-threshold networks in credit risk models. Quantitative Finance. DOI: 10.1080/14697688.2025.2465697.

Lyocsa, S., Plat, V., Gao, H. (2025). A fuzzy framework for realized volatility prediction. Journal of Forecasting. DOI: 10.1002/for.70082.

Submitted: Baals, L.J., et al. (2025). Network Evidence on Credit-Risk Pricing in P2P Lending. SSRN 5276337. Baals, L.J., et al. (2025). State-Dependent Pricing in FinTech Credit: Evidence from P2P Lending. SSRN 5421207.

### Main Publication Output (ORCID 2024-2025)

The following publications are registered in ORCID for the project researchers (2024-2025):

**Joerg Osterrieder** (ORCID: [0000-0003-0189-8636](https://orcid.org/0000-0003-0189-8636)):

1. "How can artificial intelligence help customer intelligence for credit portfolio management? A systematic literature review". International Journal of Information Management Data Insights. [DOI: 10.1016/j.jjimei.2024.100234](https://doi.org/10.1016/j.jjimei.2024.100234)

2. "Stylized facts of metaverse non-fungible tokens". Physica A: Statistical Mechanics and its Applications. [DOI: 10.1016/j.physa.2024.130103](https://doi.org/10.1016/j.physa.2024.130103)

3. "Leveraging network topology for credit risk assessment in P2P lending". Expert Systems with Applications. [DOI: 10.1016/j.eswa.2024.124100](https://doi.org/10.1016/j.eswa.2024.124100) (with Baals, Liu)

4. "Network centrality and credit risk: A comprehensive analysis of peer-to-peer lending dynamics". Finance Research Letters. [DOI: 10.1016/j.frl.2024.105308](https://doi.org/10.1016/j.frl.2024.105308) (with Baals, Liu)

5. "Towards a new PhD Curriculum for Digital Finance". Open Research Europe. [DOI: 10.12688/openreseurope.16513.1](https://doi.org/10.12688/openreseurope.16513.1) (with Liu)

6. "Visual XAI tool". Zenodo. [DOI: 10.5281/zenodo.10934115](https://doi.org/10.5281/zenodo.10934115)

7. "A discussion paper for possible approaches to building a statistically valid backtesting framework". SSRN. [DOI: 10.2139/ssrn.4893677](https://doi.org/10.2139/ssrn.4893677)

8. "Enhancing Security in Blockchain Networks: Anomalies, Frauds, and Advanced Detection Techniques". arXiv. [DOI: 10.48550/arxiv.2402.11231](https://doi.org/10.48550/arxiv.2402.11231)

9. "Ethical Artificial Intelligence, Fintech and Data Protection: A Path Forward for Training in Europe". SSRN. [DOI: 10.2139/ssrn.4885037](https://doi.org/10.2139/ssrn.4885037)

10. "Forecasting Commercial Customers Credit Risk Through Early Warning Signals Data". SSRN. [DOI: 10.2139/ssrn.4754568](https://doi.org/10.2139/ssrn.4754568)

11. "How can Consumers Without Credit History Benefit from the Use of Information Processing and Machine Learning Tools by Financial Institutions?". SSRN. [DOI: 10.2139/ssrn.4730445](https://doi.org/10.2139/ssrn.4730445)

12. "Hypothesizing Multimodal Influence: Assessing the Impact of Textual and Non-Textual Data on Financial Instrument Pricing Using NLP and Generative AI". SSRN. [DOI: 10.2139/ssrn.4698153](https://doi.org/10.2139/ssrn.4698153)

13. "Integrating Early Warning Systems with Customer Segmentation". SSRN. [DOI: 10.2139/ssrn.4779632](https://doi.org/10.2139/ssrn.4779632)

14. "Integration of Early Warning Systems and Customer Segmentation Methods in the Financial Industry - A Systematic Literature Review". SSRN. [DOI: 10.2139/ssrn.4730479](https://doi.org/10.2139/ssrn.4730479)

15. "Metaverse Non Fungible Tokens". SSRN. [DOI: 10.2139/ssrn.4733153](https://doi.org/10.2139/ssrn.4733153)

16. "Modeling Commodity Price Co-Movement: Building on Traditional Methods & Exploring Applications of Machine Learning Models". SSRN. [DOI: 10.2139/ssrn.4730474](https://doi.org/10.2139/ssrn.4730474)

17. "Predicting Retail Customers' Distress: Early Warning Systems and Machine Learning Applications". SSRN. [DOI: 10.2139/ssrn.4730470](https://doi.org/10.2139/ssrn.4730470)

**Stefan Lyocsa** (ORCID: [0000-0002-8380-181X](https://orcid.org/0000-0002-8380-181X)):

18. "Macroeconomic environment and the future performance of loans: Evidence from three peer-to-peer platforms" (2024). International Review of Financial Analysis. [DOI: 10.1016/j.irfa.2024.103416](https://doi.org/10.1016/j.irfa.2024.103416)

19. "What drives the uranium sector risk? The role of attention, economic and geopolitical uncertainty" (2024). Energy Economics. [DOI: 10.1016/j.eneco.2024.107980](https://doi.org/10.1016/j.eneco.2024.107980)

20. "Forecasting of clean energy market volatility: The role of oil and the technology sector" (2024). Energy Economics. [DOI: 10.1016/j.eneco.2024.107451](https://doi.org/10.1016/j.eneco.2024.107451)

21. "A Fuzzy Framework for Realized Volatility Prediction: Empirical Evidence From Equity Markets" (2025). Journal of Forecasting. [DOI: 10.1002/for.70082](https://doi.org/10.1002/for.70082)

22. "Alpha-threshold networks in credit risk models" (2025). Quantitative Finance. [DOI: 10.1080/14697688.2025.2465697](https://doi.org/10.1080/14697688.2025.2465697)

23. "Do hurricanes cause storm on the stock market? The case of US energy companies" (2025). International Review of Financial Analysis. [DOI: 10.1016/j.irfa.2024.103816](https://doi.org/10.1016/j.irfa.2024.103816)

**Branka Hadji Misheva** (ORCID: [0000-0001-7020-3469](https://orcid.org/0000-0001-7020-3469)):
- Co-author on publications 3, 4 above (Expert Systems with Applications, Finance Research Letters)

**Lennart John Baals** (ORCID: [0000-0002-7737-9675](https://orcid.org/0000-0002-7737-9675)):
- Co-author on publications 3, 4 above (Expert Systems with Applications, Finance Research Letters)

**Yiting Liu** (ORCID: [0009-0006-9554-8205](https://orcid.org/0009-0006-9554-8205)):
- Co-author on publications 3, 4, 5 above (Expert Systems with Applications, Finance Research Letters, Open Research Europe)

### Appendix B: Open Science Deposits (Zenodo)

{% for output in site.data.research_outputs %}
{{ output.title }}. {{ output.creators | join: ", " }} ({{ output.publication_date | slice: 0, 4 }}). {{ output.resource_type }}. [Zenodo]({{ output.zenodo_url }})
{% endfor %}

### Appendix C: Academic Events

- **December 17, 2024:** 4th International Symposium on Big Data and AI, Hong Kong - Systematic Literature Review on Graph-Based Credit Models
- **September 29, 2024:** 8th Bern Conference on Fintech and AI in Finance, Bern, Switzerland
- **September 2024:** AI Finance Insights: Pioneering the Future of Fintech, Istanbul, Turkey
- **May 20-21, 2024:** COST FinAI Meets Istanbul Conference, Turkey
- **May 2024:** COST FinAI PhD School, Treviso, Italy
- **May 2024:** COST FinAI Brussels Conference, Belgium
- **December 2023:** 16th ERCIM WG / 17th CFE Conference, Berlin, Germany
- **November 29, 2023:** BFH Doctoral Seminar, Bern, Switzerland
- **September 27-29, 2023:** 8th European COST Conference on AI in Finance, Bern, Switzerland
- **September 2023:** European Summer School in Financial Mathematics, TU Delft, Netherlands
- **September 2023:** Shenzhen Technology University International Week, China
- **June 2023:** COST Action Training School, Enschede, Netherlands

### Appendix D: Dataset

Bondora P2P Lending Dataset. Coverage: June 2009 - April 2022. Sample: 231,039 borrowers, 112 variables. DOI: 10.21227/33kz-0s65. License: CC-BY 4.0.

### Appendix E: International Collaborations

Masaryk University (Czech Republic), Columbia University (USA), American University of Sharjah (UAE), Renmin University of China (China), University of Manchester (UK).

### Appendix F: PhD Researchers

Lennart John Baals: PhD In Progress, BFH/University of Twente, Graph-based credit models and network analysis for credit risk assessment.

Yiting Liu: PhD In Progress, BFH/University of Twente, P2P lending risk modeling and network topology for credit risk.

---

Report submitted to: Swiss National Science Foundation (SNSF). Report date: December 2025. Data source: [SNSF Data Portal - Grant 205487](https://data.snf.ch/grants/grant/205487)

</div>
