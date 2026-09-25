<a id="top"></a>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="themes/amber/banner-dark.svg">
  <img alt="Francisco José Carriedo Hernández — Data Analyst & BI · Licensed Actuary" src="themes/amber/banner-light.svg" width="100%">
</picture>

</div>

<br>

<div align="center"><picture><img src="themes/amber/label-about-en.svg" alt="About me"></picture></div>

I'm a licensed actuary who moved into data. I build **end-to-end data solutions** — extracting and validating data, modeling it, and turning it into dashboards and reports people actually use. My background spans **banking, insurance, and consumer goods**, and my quantitative training leads me to treat every data point as something to validate against a source of truth: **reliable pipelines, not just results that look good.**

- Focus: Business Intelligence, data pipelines, and applied AI (LLMs / RAG)
- 1st place — **Capgemini & Microsoft Hackathon 2023** (Azure-hosted knowledge base behind a RAG)
- Engineering rigor: automated tests, static typing, clean documentation
- Spanish (native) · English (C1) · Open to Data Analyst / BI / Data Engineer roles — immediately available

<br>

**How I work**

```mermaid
flowchart LR
    subgraph SRC["&nbsp;Data sources&nbsp;"]
        direction TB
        ERP("Microsip ERP<br/>Firebird")
        DB("SQL Server<br/>PostgreSQL")
        DOC("Scanned docs<br/>invoices, IDs")
    end
    subgraph PY["&nbsp;Python processing&nbsp;"]
        direction TB
        PIPE("Pipelines<br/>pandas · SQL")
        QA("Data quality<br/>checksum · dedup<br/>fuzzy matching")
        AI("Applied AI<br/>Gemini · OCR/NLP · RAG")
    end
    subgraph OUT["&nbsp;Delivery&nbsp;"]
        direction TB
        MOD("Semantic model<br/>star schema · DAX")
        PBI("Power BI<br/>dashboards")
        XLS("Excel<br/>reports")
    end
    subgraph INFRA["&nbsp;Runs on&nbsp;"]
        CLOUD("AWS · Azure<br/>Lambda · DynamoDB · OpenAI")
        SRV("Self-hosted Linux<br/>Docker · CI/CD")
    end
    ERP --> PIPE
    DB --> PIPE
    DOC --> AI
    AI --> QA
    PIPE --> QA
    QA --> MOD
    MOD --> PBI
    MOD --> XLS
    PY -.-> INFRA
    classDef box fill:#0F3A5F,stroke:#F5A623,stroke-width:1px,color:#ffffff,rx:12,ry:12;
    class ERP,DB,DOC,PIPE,QA,AI,MOD,PBI,XLS,CLOUD,SRV box;
    classDef grp fill:#0a2740,stroke:#3a556e,color:#cddfe7;
    class SRC,PY,OUT,INFRA grp;
```

<br>

<div align="center"><picture><img src="themes/amber/label-stack-en.svg" alt="Tech stack"></picture></div>

<div align="center">

<picture><img src="https://skillicons.dev/icons?i=python,postgres,dynamodb,aws,azure,docker,linux,git,github,githubactions,bash,flask&perline=6" alt="Python, PostgreSQL, DynamoDB, AWS, Azure, Docker, Linux, Git, GitHub, GitHub Actions, Bash, Flask"></picture>

<picture><img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/microsoft-power-bi.svg" alt="Power BI" height="44"></picture>&nbsp;&nbsp;&nbsp;<picture><img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/pandas-icon.svg" alt="pandas" height="44"></picture>&nbsp;&nbsp;&nbsp;<picture><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" alt="SQL Server" height="44"></picture>&nbsp;&nbsp;&nbsp;<picture><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytest/pytest-original.svg" alt="pytest" height="44"></picture>

| Area | Tools |
|:--|:--|
| Languages & data | <kbd>Python</kbd> <kbd>SQL</kbd> <kbd>pandas</kbd> <kbd>Bash</kbd> |
| BI & visualization | <kbd>Power BI</kbd> <kbd>DAX</kbd> <kbd>Power Query</kbd> <kbd>MicroStrategy</kbd> <kbd>Excel / VBA</kbd> |
| Databases | <kbd>PostgreSQL</kbd> <kbd>SQL Server</kbd> <kbd>Firebird</kbd> <kbd>DynamoDB</kbd> |
| Cloud & applied AI | <kbd>AWS</kbd> <kbd>Azure</kbd> <kbd>LLMs / RAG</kbd> <kbd>OCR / NLP</kbd> |
| Tooling | <kbd>Git</kbd> <kbd>Docker</kbd> <kbd>Linux</kbd> <kbd>pytest</kbd> <kbd>mypy</kbd> <kbd>pydantic</kbd> |

</div>

<br>

<div align="center"><picture><img src="themes/amber/label-projects-en.svg" alt="Featured projects"></picture></div>

**cxc-report-engine**
Python engine that audits **accounts-receivable (AR)** data from the Microsip ERP (Firebird) and generates collections reports in Excel, segmented by collector. Built with engineering rigor: modular architecture, **286 `pytest` tests, `mypy --strict`, and `pydantic` schemas** for validated data models.
<kbd>Python</kbd> <kbd>Firebird</kbd> <kbd>pandas</kbd> <kbd>pytest</kbd> <kbd>mypy</kbd> <kbd>pydantic</kbd>

**gemini-document-intelligence**
Document-intelligence pipeline built on the **Google Gemini API** that classified and processed an initial batch of ~6,000 scanned invoices — with hash-based deduplication (process only new documents) and an API spend cap to control cost.
<kbd>Python</kbd> <kbd>Gemini API</kbd> <kbd>OCR / NLP</kbd>

**collections-dashboard** &nbsp; *(in progress)*
A Power BI **collections dashboard managed as code**: version-controlled in **PBIP format with TMDL**, so the semantic model, table relationships, and DAX measures live as text files under source control — enabling diffs, review, and reproducibility for the data model itself.
<kbd>Power BI</kbd> <kbd>PBIP / TMDL</kbd> <kbd>DAX</kbd> <kbd>Data modeling</kbd>

**privasee-bi** &nbsp; *(in progress)*
Self-hosted analytics platform I'm building to explore a privacy-first BI stack.
<kbd>Flask</kbd> <kbd>Docker</kbd> <kbd>Python</kbd>

> [!NOTE]
> Some professional projects are covered by confidentiality and are described in my CV rather than published here.

<br>

<div align="center"><picture><img src="themes/amber/label-certs-en.svg" alt="Certifications"></picture></div>

- Oracle Cloud Infrastructure 2024 — **AI Foundations Associate** (2024)
- Microsoft Certified — **Azure Fundamentals (AZ-900)** (2024)
- IBM — **Applied Software Engineering Fundamentals** (2026)
- GitHub Foundations (Microsoft Learn path) · Power BI Data Analyst **(PL-300, in progress)**

<br>

<div align="center">

<picture><img src="themes/amber/label-contact-en.svg" alt="Get in touch"></picture>

<br><br>

<a href="https://linkedin.com/in/carriedo"><img src="themes/amber/c-linkedin.svg" alt="LinkedIn"></a>&nbsp;
<a href="mailto:fco.carriedo@outlook.com"><img src="themes/amber/c-email.svg" alt="Email"></a>&nbsp;
<a href="https://github.com/frnc-crrd"><img src="themes/amber/c-github.svg" alt="GitHub"></a>

<br><br>

<a href="#top"><img src="themes/amber/btn-back-to-top.svg" alt="Back to top"></a>

</div>