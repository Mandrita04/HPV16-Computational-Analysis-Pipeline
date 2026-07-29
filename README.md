# HPV16 E6/E7 Computational Analysis Pipeline

## Project Overview

This project presents a comparative bioinformatics analysis of the two major Human Papillomavirus type 16 (HPV16) oncoproteins, **E6** and **E7**. Using Python and bioinformatics tools, with data sourced from NCBI, UniProt, and RCSB PDB, the pipeline investigates differences between these proteins at the **genomic, RNA, protein, structural, and evolutionary** levels.

---
## Why This Project

Human papillomavirus type 16 (HPV16) is responsible for the majority of HPV-associated cancers worldwide. Its two primary oncoproteins E6 and E7 are small, disordered, and structurally unlike classical drug targets, yet they are responsible for inactivating two of the most critical tumor suppressors in human biology: p53 and Rb.

I built this pipeline to understand E6 and E7 not just as names in a textbook, but computationally
to ask what their sequences, physicochemical profiles, BLAST conservation patterns, and 3D structural features actually reveal.

---

## Research Question
How do HPV16 oncoproteins E6 and E7 differ at the sequence, physicochemical, and structural level  and what do those differences reveal about their respective mechanisms of oncogenesis?

---

## Objectives

* Retrieve HPV16 genomic and protein data from public biological databases.
* Analyze nucleotide composition and sequence characteristics.
* Compare RNA properties, codon usage, and secondary structures.
* Characterize protein composition and physicochemical properties.
* Explore available 3D protein structures.
* Evaluate evolutionary conservation using BLAST.
* Generate visualizations and comparative summaries for E6 and E7.

---


## Repository Structure

HPV16-E6/E7-Computational-Analysis-Pipeline
* README.md 
* Data
* Pipeline    
* 01_Database_Retrieval 
* 02_BLAST_analysis 
* 03_RNA_analysis
* 04_protein_analysis  
* Output


---

## Modules Overview
### Module 01: Database Retrieval
Retrieves HPV16 RefSeq genome, parses gene annotations from GenBank format, validates CDS positions against known coordinates, fetches E6 and E7 protein records from UniProt, and downloads PDB structures programmatically.

### Module 02: BLAST Analysis
Runs remote BLASTP searches for E6 and E7 against the Papillomaviridae database, parses XML results, filters by E-value and identity thresholds, and generates comparative visualizations of bit scores and E-value distributions.

### Module 03: RNA Analysis
Converts genomic sequence to mRNA, computes codon usage tables for E6 and E7 transcripts, identifies rare codons, and runs RNA secondary structure prediction via ViennaRNA.

### Module 04: Protein Analysis
Computes physicochemical properties (MW, pI, GRAVY, instability index, aromaticity) using Biopython, parses PDB files for structural features, calculates inter residue distances for zinc finger geometry validation, and searches for known functional motifs.


---

## Technologies Used

* Python
* Biopython
* NumPy
* Pandas
* Matplotlib
* ViennaRNA
* NCBI BLAST
* UniProt
* Protein Data Bank (PDB)
* RCBS PDB

---

## Future Improvements

* Multiple Sequence Alignment (MSA)
* Phylogenetic tree construction
* Protein structure visualization using PyMOL
* Functional domain prediction
* Comparative analysis across additional high-risk HPV types
* Interactive analysis notebooks

---

