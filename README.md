# Avarodh: Enterprise AI Security Gateway

Avarodh is a Zero-Trust AI reverse proxy that acts as a secure firewall between your internal applications and public LLMs. We provide semantic caching, dynamic RBAC, and prompt injection mitigation to ensure your payloads remain secure, compliant, and cost-effective.

## 🚀 Get Started (Free Developer Tier)

Start routing your AI traffic securely in under 60 seconds. Our Developer Tier is free forever and includes **10,000 monthly proxy requests** to help you build securely from day one.

👉 **[Create your Free Workspace](https://avarodh.dev/signup)**

## Drop-in Integration

Avarodh acts as a drop-in replacement for the standard OpenAI SDK. Point your existing client to your dedicated proxy—no complex application rewrites required.

1. **Get your Workspace ID:** Log into the [Avarodh Control Plane](https://avarodh.dev), navigate to **Gateway Settings**, and copy your Workspace ID.
2. **Run the Quickstart:** Clone this repository, add your keys to the `.env` file, and execute `quickstart.py`.

## Platform Architecture

Avarodh utilizes a powerful split-plane architecture to combine SaaS convenience with enterprise-grade security.

*   **The Control Plane (Cloud):** A centralized dashboard to manage your team's RBAC, write custom data-loss prevention (DLP) guardrails, and monitor SOC2-compliant audit logs across your organization.
*   **The Data Plane (Edge):** A high-performance FastAPI proxy that intercepts requests, enforces your cloud policies using DSPy intent evaluation, and utilizes PostgreSQL/pgvector for Layer-2 semantic caching.

## Enterprise & Standard Tiers

Scaling beyond the Developer tier? We offer extended telemetry retention, unlimited custom RBAC roles, and dedicated VPC deployments for teams with strict compliance requirements. 

👉 **[View Pricing & Book a Demo](https://avarodh.dev/#pricing)**