#!/usr/bin/env python3
"""
Add PhD ORCID publications section to the existing ScientificReport_Osterrieder.docx
"""

from docx import Document
from docx.shared import Pt
from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent / "final_scientific_report" / "ScientificReport_Osterrieder.docx"
OUTPUT_PATH = Path(__file__).parent.parent / "SNSF_Report_205487.docx"

ORCID_SECTION = """Main Publication Output - PhD Researchers (ORCID)

The following publications are registered in ORCID for the project's PhD researchers:

Lennart John Baals (ORCID: 0000-0002-7737-9675):

Baals, L.J., Liu, Y. et al. (2024). "Leveraging network topology for credit risk assessment in P2P lending: A comparative study under the lens of machine learning". Expert Systems with Applications, 252, 124100. DOI: https://doi.org/10.1016/j.eswa.2024.124100

Baals, L.J., Liu, Y. et al. (2024). "Network centrality and credit risk: A comprehensive analysis of peer-to-peer lending dynamics". Finance Research Letters, 63, 105308. DOI: https://doi.org/10.1016/j.frl.2024.105308

Yiting Liu (ORCID: 0009-0006-9554-8205):

Liu, Y., Baals, L.J. et al. (2024). "Leveraging network topology for credit risk assessment in P2P lending: A comparative study under the lens of machine learning". Expert Systems with Applications, 252, 124100. DOI: https://doi.org/10.1016/j.eswa.2024.124100

Liu, Y., Baals, L.J. et al. (2024). "Network centrality and credit risk: A comprehensive analysis of peer-to-peer lending dynamics". Finance Research Letters, 63, 105308. DOI: https://doi.org/10.1016/j.frl.2024.105308

Liu, Y. et al. (2024). "Towards a new PhD Curriculum for Digital Finance". Open Research Europe, 4, 16513. DOI: https://doi.org/10.12688/openreseurope.16513.1

Liu, Y. et al. (2023). "Navigating the Environmental, Social, and Governance (ESG) landscape: constructing a robust and reliable scoring engine". Open Research Europe. DOI: https://doi.org/10.12688/openreseurope.16278.1"""

def main():
    print(f"Loading: {INPUT_PATH}")
    doc = Document(INPUT_PATH)

    # Find "Appendix B" and insert ORCID section before it
    insert_idx = None
    for i, para in enumerate(doc.paragraphs):
        if "Appendix B" in para.text:
            insert_idx = i
            break

    if insert_idx is None:
        print("Could not find 'Appendix B' - appending to end")
        insert_idx = len(doc.paragraphs)

    # Add paragraphs in reverse order (since we're inserting before Appendix B)
    paragraphs = ORCID_SECTION.strip().split('\n\n')

    # Find the element before Appendix B
    appendix_b_para = doc.paragraphs[insert_idx]

    # Insert new paragraphs before Appendix B
    prev = None
    for para_text in paragraphs:
        if para_text.strip():
            new_para = doc.add_paragraph()

            # Move to correct position
            if prev is None:
                appendix_b_para._element.addprevious(new_para._element)
            else:
                prev._element.addnext(new_para._element)
            prev = new_para

            # Check if it's a heading
            if para_text.startswith("Main Publication Output") or \
               para_text.startswith("Lennart John Baals") or \
               para_text.startswith("Yiting Liu") or \
               para_text.startswith("The following"):
                run = new_para.add_run(para_text)
                if para_text.startswith("Main Publication Output"):
                    run.bold = True
                elif para_text.startswith("Lennart") or para_text.startswith("Yiting"):
                    run.bold = True
            else:
                new_para.add_run(para_text)

    print(f"Added ORCID publications section")
    doc.save(OUTPUT_PATH)
    print(f"Saved: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
