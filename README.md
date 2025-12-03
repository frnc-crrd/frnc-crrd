# Francisco Carriedo
**Software Engineer | Quantitative Analyst | Cloud Architect**

I engineer financial-grade software solutions where mathematical precision meets distributed system scalability. With a foundation in Actuarial Science, I approach software development with a risk-aware, data-first mindset, focusing on correctness, auditability, and performance.

## Engineering Standards

I do not ship code that "just works." I ship systems that are maintainable, testable, and secure by design.

* **Architecture:** Event-Driven and Microservices (AWS/Azure) over monolithic structures.
* **Reliability:** Strict TDD cycles with Pytest; if it is not tested, it does not exist.
* **Operations:** Infrastructure as Code (Terraform/CloudFormation) and immutable deployments.
* **Data:** Zero-latency architectures using in-memory columnar processing (DuckDB/Arrow).

## Technical Arsenal

| Domain | Technologies |
| :--- | :--- |
| **Core** | Python, C# (.NET), TypeScript, SQL, Bash |
| **Compute** | AWS Lambda, Azure Functions, Docker, Kubernetes |
| **Data** | PostgreSQL, Redis, DynamoDB, DuckDB, Ibis Framework |
| **DevOps** | GitHub Actions, Azure DevOps, Terraform, SonarQube |

## Signature Architecture

### [PrivaSee BI Ecosystem]
*A self-hosted, high-performance analytics platform designed to replace legacy reporting tools.*

* **The Challenge:** Process millions of records with sub-second latency without incurring Enterprise Data Warehouse costs.
* **The Architecture:**
    * **Decoupled Storage:** Separated OLTP (PostgreSQL) from OLAP workloads to ensure data integrity.
    * **In-Memory Compute:** Utilized DuckDB and Ibis for vectorised query execution.
    * **Performance:** Achieved desktop-grade UI performance in-browser using Vizro and Plotly Dash.

### [Serverless OCR Orchestrator]
*Event-driven document ingestion pipeline for enterprise scale.*

* **The Logic:** Asynchronous processing via AWS SQS/SNS to handle burst workloads without server provisioning.
* **The Security:** Implemented rigorous IAM governance and PII redaction workflows.

## Contact

* [LinkedIn](https://www.linkedin.com/in/carriedo)
* [Email](mailto:fco.carriedo@outlook.com)
