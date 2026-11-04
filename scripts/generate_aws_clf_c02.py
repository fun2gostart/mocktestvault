import json, os

def get_questions_set1():
    # 65 questions for Set 1
    questions = []
    
    # -------------------------------------------------------------
    # DOMAIN 1: CLOUD CONCEPTS (16 Questions: Q1 - Q16)
    # -------------------------------------------------------------
    d1 = [
        {
            "id": "aws-clf02-s1-001",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Cloud Economics & TCO)",
            "difficulty": "Easy",
            "question": "Which pricing benefit allows AWS customers to pay only for the individual compute and storage services they consume, without long-term commitments or upfront fees?",
            "options": [
                "Pay-as-you-go pricing model",
                "Fixed capital expenditure allocation",
                "Perpetual enterprise software licensing",
                "Standard annualized depreciation amortizing"
            ],
            "answer": 0,
            "explanation": "AWS operates on a utility-based pay-as-you-go pricing model where customers pay exclusively for the compute capacity, storage volumes, and bandwidth consumed during the active billing period without mandatory upfront investments or long-term vendor lock-in.",
            "citation": "AWS Certified Cloud Practitioner (CLF-C02) Exam Guide — Domain 1: Cloud Concepts"
        },
        {
            "id": "aws-clf02-s1-002",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (AWS Well-Architected Framework)",
            "difficulty": "Medium",
            "question": "An enterprise wants to design its cloud workload to automatically recover from component disruptions and dynamically acquire computing resources to meet fluctuating user demand. Which pillar of the AWS Well-Architected Framework directly addresses this capability?",
            "options": [
                "Reliability Pillar",
                "Operational Excellence Pillar",
                "Cost Optimization Pillar",
                "Sustainability Pillar"
            ],
            "answer": 0,
            "explanation": "The Reliability pillar encompasses the ability of a workload to perform its intended function correctly and consistently. Key principles include testing recovery procedures, automatically recovering from failures, and scaling horizontally to increase overall system availability.",
            "citation": "AWS Well-Architected Framework — Reliability Pillar"
        },
        {
            "id": "aws-clf02-s1-003",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Agility & Elasticity)",
            "difficulty": "Easy",
            "question": "Which cloud computing characteristic describes the ability of a system to quickly provision additional server capacity during unexpected traffic spikes and automatically terminate unused resources when demand returns to normal baseline levels?",
            "options": [
                "Elasticity",
                "Static Capacity Planning",
                "High Availability",
                "Vertical Server Consolidation"
            ],
            "answer": 0,
            "explanation": "Elasticity is the ability of an infrastructure to acquire computing resources when needed and release them when no longer required, matching resource allocation directly with current real-time demand to minimize idle expenditures.",
            "citation": "AWS Cloud Practitioner Essentials — Benefits of Cloud Computing"
        },
        {
            "id": "aws-clf02-s1-004",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Global Infrastructure Topology)",
            "difficulty": "Medium",
            "question": "How is an AWS Region structured in the AWS Global Infrastructure?",
            "options": [
                "A physical geographical location containing two or more distinct, isolated Availability Zones interconnected through low-latency private fiber networks",
                "A single high-density data center facility located near a major metropolitan hub",
                "A collection of edge point-of-presence (PoP) caching servers operated by commercial telecommunication carriers",
                "A virtual cloud partition restricted to a single corporate tenant within an on-premises colocation facility"
            ],
            "answer": 0,
            "explanation": "An AWS Region is a physical geographical location in the world with multiple, isolated, and physically separated Availability Zones (AZs). Each AZ is engineered with independent power, cooling, and physical security, interconnected via high-bandwidth, low-latency private metropolitan fiber networks.",
            "citation": "AWS Global Infrastructure Documentation — Regions and Availability Zones"
        },
        {
            "id": "aws-clf02-s1-005",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (CapEx vs OpEx Financial Models)",
            "difficulty": "Easy",
            "question": "Migrating on-premises IT infrastructure workloads to the AWS Cloud allows businesses to transition from which financial expenditure model to which alternative model?",
            "options": [
                "From Capital Expenditures (CapEx) to Variable Operational Expenditures (OpEx)",
                "From Operational Expenditures (OpEx) to Capital Expenditures (CapEx)",
                "From Variable Pricing to Perpetual Capital Amortization",
                "From High Liquidity Reserves to Fixed Asset Depreciations"
            ],
            "answer": 0,
            "explanation": "Cloud computing replaces upfront Capital Expenditures (CapEx)—such as purchasing physical servers, uninterruptible power supplies, and real estate data centers—with low, variable Operational Expenditures (OpEx) that scale directly with actual business usage.",
            "citation": "AWS Cloud Value Framework — Cost Savings and Financial Flexibility"
        },
        {
            "id": "aws-clf02-s1-006",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Economies of Scale)",
            "difficulty": "Easy",
            "question": "Why can AWS offer lower pay-as-you-go pricing to its customers over time as platform adoption increases across the global marketplace?",
            "options": [
                "Massive economies of scale achieved by aggregating usage across hundreds of thousands of active customers worldwide",
                "Exclusive mandatory multi-year enterprise contracts enforced across all customer accounts",
                "Government telecommunication infrastructure subsidies provided to tier-one cloud providers",
                "Proprietary single-tenant server hardware that never requires firmware security updates"
            ],
            "answer": 0,
            "explanation": "Because AWS aggregates computing usage across hundreds of thousands of customers, it achieves higher economies of scale. These operational efficiencies translate into lower procurement and administrative costs, which AWS consistently passes back to customers through price reductions.",
            "citation": "AWS Well-Architected Framework — Principles of Cloud Economics"
        },
        {
            "id": "aws-clf02-s1-007",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Cloud Architecture Best Practices)",
            "difficulty": "Medium",
            "question": "Which core design principle is emphasized when architecting resilient, fault-tolerant cloud solutions on AWS?",
            "options": [
                "Design for failure by decoupling system components and distributing instances across multiple Availability Zones",
                "Consolidate all database and application layers onto a single large monolithic virtual machine",
                "Deploy all application services within a single data center to eliminate inter-subnet network latency",
                "Hardcode static IP addresses and physical host server bindings directly into application binaries"
            ],
            "answer": 0,
            "explanation": "A foundational tenet of cloud architecture is 'Design for Failure.' Decoupling software components using message queues (like Amazon SQS) and distributing instances across multiple Availability Zones ensures that the failure of any single component or data center does not bring down the entire system.",
            "citation": "AWS Architecture Center — Design for Failure Best Practices"
        },
        {
            "id": "aws-clf02-s1-008",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Edge Infrastructure)",
            "difficulty": "Medium",
            "question": "What is the primary purpose of an AWS Edge Location within the AWS Global Infrastructure?",
            "options": [
                "To cache static and dynamic web content closer to end-users to reduce latency via Amazon CloudFront",
                "To host primary transactional database instances for regional corporate headquarters",
                "To execute long-running batch data processing jobs on bare-metal compute instances",
                "To store on-premises physical tape backups for statutory regulatory retention compliance"
            ],
            "answer": 0,
            "explanation": "AWS Edge Locations are points of presence (PoP) deployed in major population centers around the globe. They are utilized by Amazon CloudFront (CDN) and AWS Lambda@Edge to cache and deliver content with single-digit millisecond latency to geographically dispersed end users.",
            "citation": "AWS Global Infrastructure Overview — Edge Locations"
        },
        {
            "id": "aws-clf02-s1-009",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Cloud Models: Public, Private, Hybrid)",
            "difficulty": "Easy",
            "question": "A financial institution runs its mission-critical core database in an on-premises private data center while bursting seasonal analytical batch processing jobs into Amazon EC2 instances. Which cloud deployment model does this scenario represent?",
            "options": [
                "Hybrid Cloud Deployment",
                "Community Cloud Deployment",
                "Private Cloud Only",
                "Fully Public Cloud Native Deployment"
            ],
            "answer": 0,
            "explanation": "A Hybrid Cloud deployment bridges existing on-premises data center infrastructure with public cloud resources (such as AWS), allowing organizations to extend their operations and scale workloads seamlessly between both environments.",
            "citation": "AWS Cloud Practitioner Essentials — Cloud Deployment Models"
        },
        {
            "id": "aws-clf02-s1-010",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Sustainability Pillar)",
            "difficulty": "Medium",
            "question": "Under the Sustainability pillar of the AWS Well-Architected Framework, which operational practice helps organizations minimize the environmental footprint of their cloud workloads?",
            "options": [
                "Maximizing compute utilization and selecting energy-efficient instance types like AWS Graviton",
                "Keeping idle EC2 instances continuously running at 10% CPU capacity to avoid cold-start delays",
                "Storing duplicate uncompressed raw video archives indefinitely across all regional S3 buckets",
                "Overprovisioning maximum server capacity during low-traffic off-peak nighttime hours"
            ],
            "answer": 0,
            "explanation": "The Sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads. Recommended practices include rightsizing resources, utilizing custom-designed energy-efficient processors like AWS Graviton, and scaling in compute resources when idle.",
            "citation": "AWS Well-Architected Framework — Sustainability Pillar"
        },
        {
            "id": "aws-clf02-s1-011",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Agility in IT Operations)",
            "difficulty": "Easy",
            "question": "How does the AWS Cloud promote organizational agility for enterprise software development teams?",
            "options": [
                "By reducing the time required to provision new development environments and test servers from weeks to minutes",
                "By providing free physical server delivery to local corporate offices within 24 hours",
                "By automating all application source code writing using algorithmic template generators",
                "By eliminating the need for application security scanning and integration testing"
            ],
            "answer": 0,
            "explanation": "Agility in cloud computing refers to how rapidly developers can innovate and deploy resources. Instead of waiting weeks or months to procure, rack, and cable physical servers, teams can spin up hundreds of virtual instances in minutes via the AWS Management Console, CLI, or API.",
            "citation": "AWS Business Value — Accelerating Innovation and Time to Market"
        },
        {
            "id": "aws-clf02-s1-012",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Fault Tolerance vs High Availability)",
            "difficulty": "Medium",
            "question": "A system architecture is designed so that if any individual component fails, the workload continues operating seamlessly with zero downtime and zero manual operator intervention. What property does this system possess?",
            "options": [
                "Fault Tolerance",
                "Disaster Recovery Cold Standby",
                "Scheduled Maintenance Failover",
                "Vertical Server Elasticity"
            ],
            "answer": 0,
            "explanation": "Fault Tolerance is the ability of an application to withstand component failures and remain operational with zero degradation of service or downtime. High Availability ensures minimal downtime, while Fault Tolerance guarantees zero operational disruption.",
            "citation": "AWS Architecture Center — High Availability vs Fault Tolerance"
        },
        {
            "id": "aws-clf02-s1-013",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (AWS Cloud Adoption Framework CAF)",
            "difficulty": "Medium",
            "question": "The AWS Cloud Adoption Framework (AWS CAF) organizes guidance into six perspectives. Which perspective focuses on ensuring that cloud investments accelerate business outcomes and align directly with corporate strategy?",
            "options": [
                "Business Perspective",
                "Platform Perspective",
                "Security Perspective",
                "Operations Perspective"
            ],
            "answer": 0,
            "explanation": "The Business perspective of the AWS CAF ensures that cloud adoption aligns with corporate business strategies and delivers measurable business value (such as revenue growth, cost reduction, and improved customer experience).",
            "citation": "AWS Cloud Adoption Framework (AWS CAF) Documentation"
        },
        {
            "id": "aws-clf02-s1-014",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Global Reach & Latency)",
            "difficulty": "Easy",
            "question": "A multinational e-commerce company headquartered in Seattle wants to launch an online retail platform for customers in Tokyo, Sydney, and Frankfurt with minimal network latency. What cloud capability enables this deployment?",
            "options": [
                "Global footprint with multiple geographically dispersed AWS Regions and Edge Locations",
                "Dedicated physical trans-oceanic cables leased directly to residential retail customers",
                "Overclocked server processors installed in the corporate headquarters data center",
                "Forced DNS rerouting through local government telecommunication satellite nodes"
            ],
            "answer": 0,
            "explanation": "AWS allows businesses to deploy applications globally in minutes by selecting regional data centers close to end-users (e.g., Tokyo, Sydney, Frankfurt), drastically reducing network round-trip latency.",
            "citation": "AWS Global Infrastructure Overview — Deploy Globally in Minutes"
        },
        {
            "id": "aws-clf02-s1-015",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Cost Optimization Pillar)",
            "difficulty": "Medium",
            "question": "Which principle reflects the Cost Optimization pillar of the AWS Well-Architected Framework?",
            "options": [
                "Analyze and attribute expenditure to specific business units using resource tagging and AWS Cost Allocation Tags",
                "Deploy the largest available instance tier to avoid measuring application memory usage",
                "Avoid using managed services so custom administrative automation can be developed in-house",
                "Disable CloudWatch metric alarms to eliminate logging storage costs"
            ],
            "answer": 0,
            "explanation": "A key tenet of Cost Optimization is measuring efficiency through cost attribution. Implementing a disciplined resource tagging strategy allows organizations to track and assign cloud expenditures directly to project owners and business units.",
            "citation": "AWS Well-Architected Framework — Cost Optimization Pillar"
        },
        {
            "id": "aws-clf02-s1-016",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Cloud Service Models: IaaS, PaaS, SaaS)",
            "difficulty": "Medium",
            "question": "Which cloud computing model offers the highest level of customer control over operating systems, network configuration, and server software installation?",
            "options": [
                "Infrastructure as a Service (IaaS)",
                "Platform as a Service (PaaS)",
                "Software as a Service (SaaS)",
                "Function as a Service (FaaS)"
            ],
            "answer": 0,
            "explanation": "Infrastructure as a Service (IaaS), exemplified by Amazon EC2, provides basic building blocks for cloud IT (virtual servers, storage, networking). The customer maintains complete administrative control over the guest OS, runtime environment, and installed software.",
            "citation": "AWS Cloud Practitioner Essentials — Cloud Service Models"
        }
    ]
    questions.extend(d1)
    
    # -------------------------------------------------------------
    # DOMAIN 2: SECURITY & COMPLIANCE (20 Questions: Q17 - Q36)
    # -------------------------------------------------------------
    d2 = [
        {
            "id": "aws-clf02-s1-017",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Shared Responsibility Model)",
            "difficulty": "Easy",
            "question": "According to the AWS Shared Responsibility Model, which security task is the sole responsibility of the customer when running an Amazon EC2 instance?",
            "options": [
                "Patching and updating the guest operating system installed on the EC2 instance",
                "Upgrading the physical hypervisor firmware on host servers in the data center",
                "Replacing degraded physical hard disk drives in AWS storage arrays",
                "Maintaining environmental temperature controls inside AWS data center facilities"
            ],
            "answer": 0,
            "explanation": "Under the Shared Responsibility Model, AWS is responsible for 'Security OF the Cloud' (hardware, virtualization hypervisors, and physical facilities). The customer is responsible for 'Security IN the Cloud,' which includes installing operating system patches, managing firewalls, and securing application data.",
            "citation": "AWS Shared Responsibility Model Documentation"
        },
        {
            "id": "aws-clf02-s1-018",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS IAM Best Practices)",
            "difficulty": "Easy",
            "question": "Which security best practice should be applied to protect the AWS root user account after initial creation?",
            "options": [
                "Enable Multi-Factor Authentication (MFA), delete root access keys, and use IAM users or roles for daily administrative tasks",
                "Share root user login credentials with lead engineers to ensure 24/7 administrative coverage",
                "Embed root access keys directly inside application deployment scripts for faster automation",
                "Disable password expiration requirements on the root account to prevent accidental lockout"
            ],
            "answer": 0,
            "explanation": "AWS strongly recommends securing the root user by enabling Multi-Factor Authentication (MFA), deleting root access keys, and creating dedicated IAM users or roles with least-privilege permissions for day-to-day administrative duties.",
            "citation": "AWS IAM Best Practices Guide — Root User Security"
        },
        {
            "id": "aws-clf02-s1-019",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Shield & DDoS Protection)",
            "difficulty": "Easy",
            "question": "Which managed AWS security service provides automatic, always-on Distributed Denial of Service (DDoS) protection at Layers 3 and 4 to all AWS customers at no additional cost?",
            "options": [
                "AWS Shield Standard",
                "AWS Shield Advanced",
                "AWS WAF Enterprise",
                "Amazon GuardDuty Core"
            ],
            "answer": 0,
            "explanation": "AWS Shield Standard is an automatic, always-on DDoS defense service provided at no additional charge to all AWS customers. It defends against common Layer 3 and Layer 4 infrastructure attacks, such as SYN floods and UDP reflection attacks.",
            "citation": "AWS Shield Developer Guide — Overview of Shield Standard"
        },
        {
            "id": "aws-clf02-s1-020",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS WAF - Web Application Firewall)",
            "difficulty": "Medium",
            "question": "A security engineer needs to protect a public-facing web application from Layer 7 application exploits such as SQL Injection (SQLi) and Cross-Site Scripting (XSS). Which service should be configured?",
            "options": [
                "AWS WAF (Web Application Firewall)",
                "Security Groups",
                "Network Access Control Lists (NACLs)",
                "AWS Artifact"
            ],
            "answer": 0,
            "explanation": "AWS WAF is a web application firewall that monitors HTTP/HTTPS requests at Layer 7. It allows administrators to define custom web access control lists (Web ACLs) to block malicious traffic patterns, including SQL Injection, Cross-Site Scripting, and IP rate limits.",
            "citation": "AWS WAF Developer Guide — Protecting Web Applications at Layer 7"
        },
        {
            "id": "aws-clf02-s1-021",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS IAM Roles vs Users)",
            "difficulty": "Medium",
            "question": "An application running on an Amazon EC2 instance needs to read and write objects to an Amazon S3 bucket. What is the most secure method to grant these permissions without storing hardcoded credentials on the instance?",
            "options": [
                "Assign an IAM Role to the EC2 instance with an attached policy permitting S3 access",
                "Hardcode the AWS root user access key and secret key in the application configuration file",
                "Create an IAM user for the application and store the static credentials on an unencrypted EBS volume",
                "Make the Amazon S3 bucket completely public so all virtual servers can access it anonymously"
            ],
            "answer": 0,
            "explanation": "IAM Roles provide temporary, automatically rotated security credentials via the EC2 instance metadata service (IMDS). Attaching an IAM Role to an EC2 instance eliminates the need to hardcode long-term access keys in code or configuration files.",
            "citation": "AWS IAM User Guide — Using Roles to Delegate Permissions"
        },
        {
            "id": "aws-clf02-s1-022",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Security Groups vs NACLs)",
            "difficulty": "Hard",
            "question": "Which of the following correctly describes the difference between a Security Group and a Network Access Control List (NACL) in Amazon VPC?",
            "options": [
                "Security Groups are stateful firewalls operating at the instance level; NACLs are stateless firewalls operating at the subnet level",
                "Security Groups are stateless firewalls operating at the subnet level; NACLs are stateful firewalls operating at the instance level",
                "Security Groups support both ALLOW and DENY rules; NACLs only support ALLOW rules",
                "Security Groups filter traffic at Layer 7; NACLs filter traffic exclusively at Layer 2"
            ],
            "answer": 0,
            "explanation": "Security Groups operate at the individual instance (ENI) level and are stateful: if inbound traffic is allowed, outbound response traffic is automatically allowed. In contrast, NACLs operate at the subnet boundary and are stateless: rules must be explicitly configured for both inbound and outbound traffic in numerical order.",
            "citation": "Amazon VPC User Guide — Security Groups vs Network ACLs"
        },
        {
            "id": "aws-clf02-s1-023",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS KMS - Key Management Service)",
            "difficulty": "Easy",
            "question": "Which managed AWS service enables customers to create, manage, and control cryptographic encryption keys used to encrypt data at rest across AWS storage and database services?",
            "options": [
                "AWS Key Management Service (AWS KMS)",
                "AWS Secrets Manager",
                "AWS Certificate Manager (ACM)",
                "AWS Systems Manager Parameter Store"
            ],
            "answer": 0,
            "explanation": "AWS Key Management Service (AWS KMS) makes it easy to create and manage cryptographic keys and control their use across a wide range of AWS services (including S3, EBS, and RDS) and within customer applications.",
            "citation": "AWS Key Management Service (AWS KMS) Overview"
        },
        {
            "id": "aws-clf02-s1-024",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Principle of Least Privilege)",
            "difficulty": "Easy",
            "question": "What core security principle states that users and services should be granted only the minimal permissions necessary to perform their required job functions?",
            "options": [
                "Principle of Least Privilege",
                "Defense-in-Depth Principle",
                "Zero Trust Network Isolation",
                "Separation of Environmental Domains"
            ],
            "answer": 0,
            "explanation": "The Principle of Least Privilege dictates that identities (users, groups, roles) are granted only the precise permissions required to perform their designated tasks—and no more. This restricts the potential blast radius of compromised credentials.",
            "citation": "AWS Security Best Practices — Granting Least Privilege"
        },
        {
            "id": "aws-clf02-s1-025",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Artifact & Compliance Reports)",
            "difficulty": "Easy",
            "question": "An enterprise audit team requires immediate on-demand access to AWS compliance documentation, including SOC 1/2/3 reports and PCI DSS certifications. Which portal provides these documents?",
            "options": [
                "AWS Artifact",
                "AWS Trusted Advisor",
                "Amazon Inspector",
                "AWS Service Catalog"
            ],
            "answer": 0,
            "explanation": "AWS Artifact is a self-service compliance portal that provides on-demand access to AWS security and compliance reports (such as SOC, ISO, and PCI DSS reports) and regulatory agreements.",
            "citation": "AWS Artifact User Guide — Compliance Reports and Agreements"
        },
        {
            "id": "aws-clf02-s1-026",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS CloudTrail - Governance & Auditing)",
            "difficulty": "Medium",
            "question": "A security analyst needs to determine which IAM user terminated a production EC2 instance three days ago. Which service records this API activity?",
            "options": [
                "AWS CloudTrail",
                "Amazon CloudWatch Logs",
                "AWS X-Ray",
                "AWS Trusted Advisor"
            ],
            "answer": 0,
            "explanation": "AWS CloudTrail records actions taken by users, roles, and AWS services as events. It logs API calls made via the AWS Management Console, SDKs, CLI tools, and higher-level services, including the caller's identity, timestamp, source IP, and parameters.",
            "citation": "AWS CloudTrail User Guide — Logging Management Events"
        },
        {
            "id": "aws-clf02-s1-027",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Amazon GuardDuty - Threat Detection)",
            "difficulty": "Medium",
            "question": "Which intelligent threat detection service continuously analyzes VPC Flow Logs, AWS CloudTrail event logs, and DNS query logs using machine learning to identify unauthorized or anomalous activity?",
            "options": [
                "Amazon GuardDuty",
                "Amazon Inspector",
                "AWS Macie",
                "AWS Config"
            ],
            "answer": 0,
            "explanation": "Amazon GuardDuty is an agentless, continuous security monitoring service that uses machine learning and anomaly detection across foundational data sources (CloudTrail, VPC Flow Logs, DNS logs, and EKS audit logs) to detect compromised instances and unauthorized account behavior.",
            "citation": "Amazon GuardDuty Documentation — Intelligent Threat Detection"
        },
        {
            "id": "aws-clf02-s1-028",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Amazon Inspector - Vulnerability Scanning)",
            "difficulty": "Medium",
            "question": "Which automated security assessment service scans Amazon EC2 instances, AWS Lambda functions, and container images in Amazon ECR for known software vulnerabilities and unintended network exposure?",
            "options": [
                "Amazon Inspector",
                "Amazon GuardDuty",
                "AWS Secrets Manager",
                "AWS Shield"
            ],
            "answer": 0,
            "explanation": "Amazon Inspector is an automated vulnerability management service that continually scans EC2 instances, container images stored in Amazon ECR, and Lambda functions for software CVEs and unintended network exposure.",
            "citation": "Amazon Inspector User Guide — Automated Vulnerability Management"
        },
        {
            "id": "aws-clf02-s1-029",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Organizations & SCPs)",
            "difficulty": "Hard",
            "question": "What is the primary function of a Service Control Policy (SCP) within AWS Organizations?",
            "options": [
                "To define the maximum permissions boundary for member accounts in an organization or organizational unit (OU)",
                "To grant administrative IAM permissions directly to individual developers in single accounts",
                "To automatically configure VPC peering connections between all member AWS accounts",
                "To encrypt all EBS volumes across member accounts using a single universal KMS key"
            ],
            "answer": 0,
            "explanation": "Service Control Policies (SCPs) are governance policies in AWS Organizations that specify the maximum permissions boundary for member accounts. Even an account root user cannot perform an action that is explicitly denied by an SCP attached to their account or OU.",
            "citation": "AWS Organizations User Guide — Service Control Policies (SCPs)"
        },
        {
            "id": "aws-clf02-s1-030",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Secrets Manager)",
            "difficulty": "Medium",
            "question": "Which AWS service helps developers securely store, rotate, manage, and retrieve database credentials and API keys with built-in automatic rotation for Amazon RDS?",
            "options": [
                "AWS Secrets Manager",
                "AWS Systems Manager Parameter Store Standard",
                "Amazon S3 Client-Side Encryption",
                "AWS IAM Credential Report"
            ],
            "answer": 0,
            "explanation": "AWS Secrets Manager helps protect secrets needed to access applications and services. It provides native, automatic rotation for Amazon RDS, Amazon Redshift, and Amazon DocumentDB credentials via AWS Lambda functions.",
            "citation": "AWS Secrets Manager User Guide — Rotating Database Credentials"
        },
        {
            "id": "aws-clf02-s1-031",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Amazon Macie - Sensitive Data Discovery)",
            "difficulty": "Medium",
            "question": "A healthcare provider needs to discover and protect Personally Identifiable Information (PII) and patient records stored inside multiple Amazon S3 buckets. Which service should be deployed?",
            "options": [
                "Amazon Macie",
                "Amazon GuardDuty",
                "AWS CloudTrail",
                "AWS KMS"
            ],
            "answer": 0,
            "explanation": "Amazon Macie is a data security and data privacy service that uses machine learning and pattern matching to discover, classify, and protect sensitive data (such as PII, credit card numbers, and medical identifiers) in Amazon S3.",
            "citation": "Amazon Macie User Guide — Discovering Sensitive Data in S3"
        },
        {
            "id": "aws-clf02-s1-032",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Config - Resource Compliance)",
            "difficulty": "Medium",
            "question": "Which service continuously evaluates, audits, and records configurations of AWS resources against predefined desired state rules (for example, ensuring that all EBS volumes are encrypted)?",
            "options": [
                "AWS Config",
                "AWS CloudTrail",
                "Amazon CloudWatch",
                "AWS Trusted Advisor"
            ],
            "answer": 0,
            "explanation": "AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. It records resource configuration changes and compares them against desired compliance rules.",
            "citation": "AWS Config Developer Guide — Tracking Resource Configurations"
        },
        {
            "id": "aws-clf02-s1-033",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Trusted Advisor - Security Pillar)",
            "difficulty": "Easy",
            "question": "Which check is provided to ALL AWS customers (including those on the Basic Support plan) by AWS Trusted Advisor?",
            "options": [
                "Review of Amazon S3 bucket permissions for open public access and root account MFA status",
                "Full architectural review of custom database read replica latency",
                "Automated penetration testing of public EC2 elastic network interfaces",
                "Real-time malware payload scanning of customer application source code"
            ],
            "answer": 0,
            "explanation": "All AWS customers have access to the Core Trusted Advisor checks, which include high-priority security checks such as Amazon S3 Bucket Permissions (identifying buckets with open public access) and MFA on the Root Account.",
            "citation": "AWS Trusted Advisor Documentation — Core Security Checks"
        },
        {
            "id": "aws-clf02-s1-034",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Penetration Testing on AWS)",
            "difficulty": "Medium",
            "question": "Under current AWS penetration testing policy, for which user-owned services can customers conduct security assessments without prior authorization from AWS?",
            "options": [
                "Customer-owned Amazon EC2 instances, Amazon RDS databases, and Amazon API Gateway endpoints",
                "AWS physical data center buildings and security badge entry systems",
                "Amazon Route 53 global DNS server fleet hardware",
                "AWS Snowmobile physical transport containers"
            ],
            "answer": 0,
            "explanation": "AWS allows customers to perform security assessments and penetration tests against eight designated customer-owned services (including EC2, RDS, CloudFront, Aurora, API Gateway, and Lambda) without prior approval from AWS.",
            "citation": "AWS Customer Support Policy — Penetration Testing"
        },
        {
            "id": "aws-clf02-s1-035",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Data Encryption at Rest and in Transit)",
            "difficulty": "Easy",
            "question": "Which protocol is standardly used to ensure that data sent between client web browsers and web servers hosted on AWS is encrypted in transit?",
            "options": [
                "Transport Layer Security (TLS / HTTPS)",
                "File Transfer Protocol (FTP)",
                "Server Message Block (SMB v1)",
                "Telnet over Port 23"
            ],
            "answer": 0,
            "explanation": "Transport Layer Security (TLS), commonly known as HTTPS, is the industry-standard cryptographic protocol used to encrypt network data in transit between clients and servers.",
            "citation": "AWS Security Best Practices — Protecting Data in Transit"
        },
        {
            "id": "aws-clf02-s1-036",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Shared Responsibility for Managed DBs)",
            "difficulty": "Medium",
            "question": "When deploying an Amazon RDS managed database, which administrative task remains the responsibility of the customer?",
            "options": [
                "Optimizing database user permissions, table indexes, and application SQL queries",
                "Installing operating system security patches on the underlying database host server",
                "Replacing failed physical hard disks in the underlying database storage cluster",
                "Managing power and physical security in the data center housing the database"
            ],
            "answer": 0,
            "explanation": "In a managed database service like Amazon RDS, AWS manages the underlying operating system, server hardware, automated software patching, and physical storage. The customer remains responsible for database schema design, indexing, SQL queries, user privileges, and network firewalls.",
            "citation": "Amazon RDS Documentation — Shared Responsibility Model for RDS"
        }
    ]
    questions.extend(d2)

    # -------------------------------------------------------------
    # DOMAIN 3: CLOUD TECHNOLOGY & SERVICES (22 Questions: Q37 - Q58)
    # -------------------------------------------------------------
    d3 = [
        {
            "id": "aws-clf02-s1-037",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon EC2 Purchasing Options)",
            "difficulty": "Medium",
            "question": "A data science team needs to run fault-tolerant batch processing workloads that can be interrupted at any time without negative business consequences. Which Amazon EC2 purchasing option offers the steepest discount (up to 90%) for this use case?",
            "options": [
                "Spot Instances",
                "On-Demand Instances",
                "Dedicated Hosts",
                "Standard 1-Year Reserved Instances"
            ],
            "answer": 0,
            "explanation": "Amazon EC2 Spot Instances allow customers to bid on unused EC2 capacity at steep discounts of up to 90% off On-Demand prices. Because AWS can reclaim Spot Instances with a 2-minute notice when capacity is needed, they are ideal for stateless, fault-tolerant workloads.",
            "citation": "Amazon EC2 Pricing Guide — Spot Instances"
        },
        {
            "id": "aws-clf02-s1-038",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Serverless Compute: AWS Lambda)",
            "difficulty": "Easy",
            "question": "Which compute service enables developers to run backend code in response to events without provisioning, managing, or scaling virtual servers?",
            "options": [
                "AWS Lambda",
                "Amazon EC2",
                "AWS Elastic Beanstalk",
                "Amazon Lightsail"
            ],
            "answer": 0,
            "explanation": "AWS Lambda is a serverless, event-driven compute service that runs code in response to triggers (such as S3 uploads or API calls) and automatically manages the underlying compute infrastructure, scaling from zero to thousands of concurrent executions.",
            "citation": "AWS Lambda Developer Guide — Serverless Compute Overview"
        },
        {
            "id": "aws-clf02-s1-039",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon S3 Storage Classes)",
            "difficulty": "Medium",
            "question": "Which Amazon S3 storage class automatically optimizes customer storage costs by moving data between frequent and infrequent access tiers based on changing usage patterns without operational overhead or retrieval fees?",
            "options": [
                "S3 Intelligent-Tiering",
                "S3 Standard-Infrequent Access (S3 Standard-IA)",
                "S3 Glacier Flexible Retrieval",
                "S3 One Zone-IA"
            ],
            "answer": 0,
            "explanation": "S3 Intelligent-Tiering is the only cloud storage class that delivers automatic cost savings by moving objects between three access tiers (Frequent, Infrequent, and Archive Instant Access) when access patterns change, with zero retrieval charges.",
            "citation": "Amazon S3 Storage Classes Guide — Intelligent-Tiering"
        },
        {
            "id": "aws-clf02-s1-040",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon EBS - Elastic Block Store)",
            "difficulty": "Easy",
            "question": "Which storage service provides high-performance, persistent block-level storage volumes designed to be attached to a single Amazon EC2 instance within the same Availability Zone?",
            "options": [
                "Amazon Elastic Block Store (Amazon EBS)",
                "Amazon Simple Storage Service (Amazon S3)",
                "AWS Storage Gateway",
                "Amazon Elastic File System (Amazon EFS)"
            ],
            "answer": 0,
            "explanation": "Amazon EBS provides block-level storage volumes for use with EC2 instances. EBS volumes behave like raw, unformatted physical hard drives and persist independently from the lifecycle of an EC2 instance.",
            "citation": "Amazon EBS User Guide — Overview of Block Storage"
        },
        {
            "id": "aws-clf02-s1-041",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon EFS - Elastic File System)",
            "difficulty": "Medium",
            "question": "An enterprise requires a serverless, POSIX-compliant shared file system that can be mounted simultaneously by hundreds of Amazon EC2 instances running Linux across multiple Availability Zones. Which service fits this requirement?",
            "options": [
                "Amazon Elastic File System (Amazon EFS)",
                "Amazon Elastic Block Store (Amazon EBS)",
                "Amazon S3 Glacier Deep Archive",
                "AWS Snowcone"
            ],
            "answer": 0,
            "explanation": "Amazon EFS is a serverless, fully elastic Network File System (NFS) that can be concurrently mounted by hundreds of EC2 Linux instances across multiple Availability Zones, scaling storage capacity automatically.",
            "citation": "Amazon EFS User Guide — Shared File Storage"
        },
        {
            "id": "aws-clf02-s1-042",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon RDS Multi-AZ vs Read Replicas)",
            "difficulty": "Hard",
            "question": "What is the primary architectural objective of configuring an Amazon RDS deployment with a Multi-AZ standby replica compared to configuring Read Replicas?",
            "options": [
                "Multi-AZ provides synchronous replication for high availability and automatic disaster failover, whereas Read Replicas provide asynchronous replication for read performance scalability",
                "Multi-AZ reduces read latency for analytics queries, whereas Read Replicas provide automated disaster failover",
                "Multi-AZ allows cross-region geographical data distribution, whereas Read Replicas are strictly confined to a single private subnet",
                "Multi-AZ is exclusively used for NoSQL databases, whereas Read Replicas are used for relational databases"
            ],
            "answer": 0,
            "explanation": "Amazon RDS Multi-AZ synchronously replicates data to a standby instance in a different Availability Zone for high availability and automated failover in the event of an outage. Read Replicas asynchronously replicate data to offload read-heavy traffic and improve performance.",
            "citation": "Amazon RDS User Guide — High Availability (Multi-AZ) vs Read Replicas"
        },
        {
            "id": "aws-clf02-s1-043",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon DynamoDB - Managed NoSQL)",
            "difficulty": "Easy",
            "question": "Which fully managed NoSQL database service delivers single-digit millisecond latency performance at any scale with seamless support for key-value and document data structures?",
            "options": [
                "Amazon DynamoDB",
                "Amazon RDS for PostgreSQL",
                "Amazon Redshift",
                "Amazon Aurora Serverless MySQL"
            ],
            "answer": 0,
            "explanation": "Amazon DynamoDB is a fully managed, serverless NoSQL key-value and document database that provides consistent, single-digit millisecond latency performance at massive petabyte scale with built-in multi-region replication via Global Tables.",
            "citation": "Amazon DynamoDB Developer Guide — Core Features"
        },
        {
            "id": "aws-clf02-s1-044",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon Aurora - Cloud-Native Relational)",
            "difficulty": "Medium",
            "question": "Which MySQL- and PostgreSQL-compatible relational database engine built specifically for the cloud delivers up to 5 times the throughput of standard MySQL while replicating data 6 times across 3 Availability Zones?",
            "options": [
                "Amazon Aurora",
                "Amazon DocumentDB",
                "Amazon Neptune",
                "Amazon ElastiCache"
            ],
            "answer": 0,
            "explanation": "Amazon Aurora is a cloud-native relational database service compatible with MySQL and PostgreSQL. It delivers up to 5x the throughput of standard MySQL and automatically replicates 6 copies of your data across 3 Availability Zones.",
            "citation": "Amazon Aurora User Guide — High Availability and Replication"
        },
        {
            "id": "aws-clf02-s1-045",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon Redshift - Data Warehousing)",
            "difficulty": "Easy",
            "question": "A business intelligence team needs to run complex SQL analytical queries across petabytes of structured historical sales data. Which columnar data warehouse service should be selected?",
            "options": [
                "Amazon Redshift",
                "Amazon DynamoDB",
                "Amazon ElastiCache for Redis",
                "Amazon QuickSight"
            ],
            "answer": 0,
            "explanation": "Amazon Redshift is a fast, fully managed cloud data warehouse that uses columnar storage and massively parallel processing (MPP) to execute complex Online Analytical Processing (OLAP) queries across petabytes of data.",
            "citation": "Amazon Redshift Database Developer Guide — OLAP Architecture"
        },
        {
            "id": "aws-clf02-s1-046",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon ElastiCache - In-Memory Caching)",
            "difficulty": "Easy",
            "question": "Which service should an architect implement to improve web application latency by caching frequently accessed database query results in memory using Redis or Memcached?",
            "options": [
                "Amazon ElastiCache",
                "Amazon CloudFront",
                "AWS Direct Connect",
                "Amazon Route 53"
            ],
            "answer": 0,
            "explanation": "Amazon ElastiCache is a fully managed in-memory data store service compatible with Redis and Memcached. Caching frequent database reads in ElastiCache delivers sub-millisecond response times and offloads traffic from underlying databases.",
            "citation": "Amazon ElastiCache User Guide — In-Memory Caching Strategies"
        },
        {
            "id": "aws-clf02-s1-047",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon VPC - Virtual Private Cloud)",
            "difficulty": "Medium",
            "question": "What is the primary function of an Amazon Virtual Private Cloud (Amazon VPC)?",
            "options": [
                "To provision a logically isolated section of the AWS Cloud where customers can launch resources in a custom virtual network",
                "To connect customer on-premises offices to physical data center power grids",
                "To automatically translate application source code into container microservices",
                "To manage multi-tenant domain name registrations and SSL certificates"
            ],
            "answer": 0,
            "explanation": "Amazon VPC lets you provision a logically isolated section of the AWS Cloud where you can define your own IP address range, subnets, route tables, and network gateways to host your cloud resources securely.",
            "citation": "Amazon VPC User Guide — What Is Amazon VPC?"
        },
        {
            "id": "aws-clf02-s1-048",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Internet Gateway vs NAT Gateway)",
            "difficulty": "Hard",
            "question": "In an Amazon VPC, which component enables backend EC2 instances located in a private subnet to initiate outbound connections to the internet for software patches while preventing inbound traffic from the internet?",
            "options": [
                "NAT Gateway",
                "Internet Gateway",
                "Virtual Private Gateway",
                "Egress-Only Internet Gateway for IPv4"
            ],
            "answer": 0,
            "explanation": "A NAT (Network Address Translation) Gateway resides in a public subnet and allows instances in private subnets to connect outbound to the internet (for software updates or external APIs) while blocking inbound traffic initiated from outside the VPC.",
            "citation": "Amazon VPC User Guide — NAT Gateways"
        },
        {
            "id": "aws-clf02-s1-049",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon Route 53 - Cloud DNS)",
            "difficulty": "Medium",
            "question": "Which highly available and scalable cloud Domain Name System (DNS) web service translates human-readable domain names (such as example.com) into numeric IP addresses while supporting health checks and failover routing?",
            "options": [
                "Amazon Route 53",
                "AWS Direct Connect",
                "Amazon CloudFront",
                "AWS Global Accelerator"
            ],
            "answer": 0,
            "explanation": "Amazon Route 53 is AWS's authoritative cloud DNS service. It provides domain registration, DNS routing (simple, latency, weighted, failover, geoproximity), and continuous health checks to route end-user traffic to healthy endpoints.",
            "citation": "Amazon Route 53 Developer Guide — Routing Policies"
        },
        {
            "id": "aws-clf02-s1-050",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon CloudFront - CDN)",
            "difficulty": "Easy",
            "question": "Which content delivery network (CDN) service securely delivers data, videos, applications, and APIs to global customers with low latency and high transfer speeds via a worldwide network of edge locations?",
            "options": [
                "Amazon CloudFront",
                "AWS Direct Connect",
                "AWS Transit Gateway",
                "Amazon API Gateway"
            ],
            "answer": 0,
            "explanation": "Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.",
            "citation": "Amazon CloudFront Developer Guide — Content Delivery Overview"
        },
        {
            "id": "aws-clf02-s1-051",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS Direct Connect - Hybrid Connectivity)",
            "difficulty": "Medium",
            "question": "A corporation requires a dedicated, private physical network connection between its on-premises corporate data center and AWS, completely bypassing the public internet for consistent bandwidth and heightened security. Which service provides this?",
            "options": [
                "AWS Direct Connect",
                "AWS Site-to-Site VPN",
                "Amazon VPC Peering",
                "AWS Transit Gateway over Public Internet"
            ],
            "answer": 0,
            "explanation": "AWS Direct Connect links an internal corporate network to an AWS Direct Connect location over a dedicated 1 Gbps, 10 Gbps, or 100 Gbps fiber-optic cable, bypassing the public internet for consistent network performance and lower data transfer costs.",
            "citation": "AWS Direct Connect User Guide — Dedicated Private Connectivity"
        },
        {
            "id": "aws-clf02-s1-052",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS CloudFormation - Infrastructure as Code)",
            "difficulty": "Easy",
            "question": "Which Infrastructure as Code (IaC) service allows architects to model, provision, and version AWS and third-party cloud resources using declarative JSON or YAML formatted templates?",
            "options": [
                "AWS CloudFormation",
                "AWS Elastic Beanstalk",
                "AWS CodeDeploy",
                "AWS Systems Manager"
            ],
            "answer": 0,
            "explanation": "AWS CloudFormation allows you to model, provision, and manage AWS and third-party resources by treating infrastructure as code. You describe all the desired resources and their dependencies in a single declarative template file (JSON or YAML).",
            "citation": "AWS CloudFormation User Guide — Infrastructure as Code Overview"
        },
        {
            "id": "aws-clf02-s1-053",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon SQS vs Amazon SNS)",
            "difficulty": "Medium",
            "question": "What is the primary operational distinction between Amazon Simple Queue Service (Amazon SQS) and Amazon Simple Notification Service (Amazon SNS)?",
            "options": [
                "Amazon SQS uses a pull/polling message retrieval mechanism for decoupled consumers; Amazon SNS uses a push-based pub/sub broadcast mechanism to multiple subscribers",
                "Amazon SQS is strictly used for audio streaming; Amazon SNS is strictly used for relational database backups",
                "Amazon SQS requires dedicated virtual machines; Amazon SNS operates completely in-memory on local hosts",
                "Amazon SQS only supports email delivery; Amazon SNS only supports SMS text messaging"
            ],
            "answer": 0,
            "explanation": "Amazon SQS is a message queuing service where worker applications poll (pull) messages from a queue for asynchronous processing. Amazon SNS is a publish/subscribe (pub/sub) service where publishers send messages that are immediately pushed to multiple subscribers (such as HTTP endpoints, email, SMS, or SQS queues).",
            "citation": "AWS Messaging Guide — SQS Queues vs SNS Topics"
        },
        {
            "id": "aws-clf02-s1-054",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS Elastic Beanstalk - PaaS)",
            "difficulty": "Easy",
            "question": "Which Platform as a Service (PaaS) offering allows developers to quickly deploy web applications written in Java, .NET, Node.js, Python, or Docker without managing the underlying EC2, Auto Scaling, and load balancing infrastructure?",
            "options": [
                "AWS Elastic Beanstalk",
                "AWS CloudFormation",
                "AWS CodePipeline",
                "AWS Batch"
            ],
            "answer": 0,
            "explanation": "AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services. Developers simply upload their application code, and Elastic Beanstalk automatically handles the deployment details: capacity provisioning, load balancing, auto-scaling, and health monitoring.",
            "citation": "AWS Elastic Beanstalk Developer Guide — PaaS Architecture"
        },
        {
            "id": "aws-clf02-s1-055",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon ECS vs Amazon EKS)",
            "difficulty": "Medium",
            "question": "An enterprise container engineering team wants to orchestrate microservice containers using open-source Kubernetes APIs and tooling on AWS. Which managed container service should they select?",
            "options": [
                "Amazon Elastic Kubernetes Service (Amazon EKS)",
                "Amazon Elastic Container Service (Amazon ECS)",
                "AWS Elastic Beanstalk",
                "Amazon Lightsail Containers"
            ],
            "answer": 0,
            "explanation": "Amazon Elastic Kubernetes Service (Amazon EKS) is a managed container service to run and scale Kubernetes applications in the cloud or on-premises, providing full compatibility with the open-source Kubernetes ecosystem and tooling.",
            "citation": "Amazon EKS User Guide — Managed Kubernetes on AWS"
        },
        {
            "id": "aws-clf02-s1-056",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon CloudWatch - Metrics & Alarms)",
            "difficulty": "Easy",
            "question": "Which monitoring service collects raw metrics (such as CPU utilization, disk I/O, and network throughput) from AWS resources and allows administrators to set automated threshold alarms?",
            "options": [
                "Amazon CloudWatch",
                "AWS CloudTrail",
                "AWS X-Ray",
                "AWS Health Dashboard"
            ],
            "answer": 0,
            "explanation": "Amazon CloudWatch is a monitoring and observability service that collects monitoring and operational data in the form of logs, metrics, and events. It enables alarms that automatically trigger auto-scaling actions or SNS notifications when thresholds are crossed.",
            "citation": "Amazon CloudWatch User Guide — Metrics and Alarms"
        },
        {
            "id": "aws-clf02-s1-057",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS Snow Family - Offline Data Transfer)",
            "difficulty": "Medium",
            "question": "A research organization needs to migrate 80 Terabytes of offline scientific survey data from a remote research vessel with limited internet connectivity into Amazon S3. Which ruggedized physical appliance is designed for this use case?",
            "options": [
                "AWS Snowball Edge",
                "AWS Direct Connect",
                "AWS Storage Gateway Volume Gateway",
                "Amazon S3 Transfer Acceleration"
            ],
            "answer": 0,
            "explanation": "AWS Snowball Edge is a ruggedized physical data transport and edge computing device that can transport up to 80 TB of data securely to AWS via courier, bypassing local network bandwidth constraints.",
            "citation": "AWS Snow Family User Guide — Snowball Edge Overview"
        },
        {
            "id": "aws-clf02-s1-058",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS X-Ray - Distributed Tracing)",
            "difficulty": "Medium",
            "question": "Which developer service helps engineers analyze, trace, and debug distributed microservice applications to identify performance bottlenecks and downstream latency root causes?",
            "options": [
                "AWS X-Ray",
                "Amazon CloudWatch Synthetics",
                "AWS CloudTrail Insights",
                "AWS AppConfig"
            ],
            "answer": 0,
            "explanation": "AWS X-Ray helps developers analyze and debug distributed applications, such as those built using a microservices architecture. It provides an end-to-end view of requests traveling through an application to identify latency bottlenecks and errors.",
            "citation": "AWS X-Ray Developer Guide — Distributed Tracing Overview"
        }
    ]
    questions.extend(d3)

    # -------------------------------------------------------------
    # DOMAIN 4: BILLING, PRICING & SUPPORT (7 Questions: Q59 - Q65)
    # -------------------------------------------------------------
    d4 = [
        {
            "id": "aws-clf02-s1-059",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Cost Explorer)",
            "difficulty": "Easy",
            "question": "Which billing tool enables customers to visualize, understand, and manage their AWS costs and usage over time, including viewing historical trends and forecasting future spending up to 12 months in advance?",
            "options": [
                "AWS Cost Explorer",
                "AWS Pricing Calculator",
                "AWS Billing Conductor",
                "AWS Marketplace Dashboard"
            ],
            "answer": 0,
            "explanation": "AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time. It provides default reports, custom filtering, and spending forecasts for the next 12 months.",
            "citation": "AWS Cost Management User Guide — Analyzing Costs with Cost Explorer"
        },
        {
            "id": "aws-clf02-s1-060",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Budgets)",
            "difficulty": "Easy",
            "question": "An IT manager wants to receive an automated email notification whenever their monthly AWS account spend exceeds 80% of their $5,000 allocated budget. Which service should be configured?",
            "options": [
                "AWS Budgets",
                "AWS Cost Explorer",
                "AWS Pricing Calculator",
                "AWS Organizations Consolidated Billing"
            ],
            "answer": 0,
            "explanation": "AWS Budgets allows you to set custom cost and usage budgets and automatically notifies you via email or Amazon SNS when your actual or forecasted usage exceeds your specified threshold percentage.",
            "citation": "AWS Cost Management Guide — Managing Budgets"
        },
        {
            "id": "aws-clf02-s1-061",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Pricing Calculator)",
            "difficulty": "Easy",
            "question": "Before migrating an on-premises workload to AWS, which free web tool can an enterprise use to model architecture solutions and estimate total monthly and annual cloud costs?",
            "options": [
                "AWS Pricing Calculator",
                "AWS Cost and Usage Report (CUR)",
                "AWS Trusted Advisor Cost Pillar",
                "AWS CloudTrail Log Analyzer"
            ],
            "answer": 0,
            "explanation": "The AWS Pricing Calculator is a free web-based planning tool that allows you to model proposed architectural workloads, estimate monthly costs, and explore pricing options before provisioning resources.",
            "citation": "AWS Pricing Calculator User Guide — Pre-Deployment Estimation"
        },
        {
            "id": "aws-clf02-s1-062",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (Consolidated Billing in AWS Organizations)",
            "difficulty": "Medium",
            "question": "What is a primary financial benefit of using Consolidated Billing within AWS Organizations?",
            "options": [
                "Aggregating usage across all member accounts to qualify for tiered volume pricing discounts on S3 and EC2",
                "Automatic conversion of all On-Demand instances into free Spot instances",
                "Elimination of all data transfer fees between global AWS regions",
                "Mandatory quarterly cost subsidies credited directly by AWS finance teams"
            ],
            "answer": 0,
            "explanation": "Consolidated Billing aggregates usage across all member accounts in an organization into a single monthly bill. This aggregation allows the organization to qualify for tiered volume pricing discounts (e.g., for Amazon S3 storage and data transfer) that individual accounts might not reach alone.",
            "citation": "AWS Organizations User Guide — Consolidated Billing Benefits"
        },
        {
            "id": "aws-clf02-s1-063",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Support Plans: Business Plan)",
            "difficulty": "Medium",
            "question": "Which AWS Support Plan provides 24/7 phone, chat, and email access to Cloud Support Engineers with a guaranteed response time of under 1 hour for production-down events, plus access to the full suite of AWS Trusted Advisor checks?",
            "options": [
                "AWS Business Support",
                "AWS Developer Support",
                "AWS Basic Support",
                "AWS Free Community Tier"
            ],
            "answer": 0,
            "explanation": "The AWS Business Support plan offers 24/7 phone, email, and chat access to Cloud Support Engineers, a < 1-hour response time SLA for production system outages, and full access to all AWS Trusted Advisor checks.",
            "citation": "AWS Support Plans Comparison Guide — Business Support"
        },
        {
            "id": "aws-clf02-s1-064",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Support Plans: Enterprise Plan & TAM)",
            "difficulty": "Medium",
            "question": "Which dedicated role is assigned exclusively to customers on the AWS Enterprise Support plan to provide architectural guidance, proactive operational reviews, and coordinate support escalations?",
            "options": [
                "Technical Account Manager (TAM)",
                "AWS Solutions Architect General Associate",
                "Dedicated Data Center Site Technician",
                "Independent Third-Party Compliance Auditor"
            ],
            "answer": 0,
            "explanation": "The Technical Account Manager (TAM) is a primary point of contact assigned exclusively to Enterprise Support customers (and pooled for Enterprise On-Ramp) to provide proactive architectural guidance, conduct operational reviews, and assist during planning.",
            "citation": "AWS Enterprise Support Overview — Role of the Technical Account Manager"
        },
        {
            "id": "aws-clf02-s1-065",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Cost and Usage Report - CUR)",
            "difficulty": "Hard",
            "question": "Which AWS billing deliverable provides the most granular, detailed raw metadata regarding cloud resource usage, pricing, and cost allocation tags, delivered daily to an Amazon S3 bucket for in-depth business intelligence analysis?",
            "options": [
                "AWS Cost and Usage Report (AWS CUR)",
                "Monthly PDF Billing Summary Invoice",
                "AWS Cost Explorer High-Level CSV Export",
                "AWS Budgets Email Digest"
            ],
            "answer": 0,
            "explanation": "The AWS Cost and Usage Report (CUR) is the most comprehensive tool for delivering raw billing datasets to an Amazon S3 bucket. It lists detailed usage down to the hour or day, categorized by product, resource ID, operation, and user-defined cost allocation tags.",
            "citation": "AWS Cost Management Guide — Cost and Usage Reports (CUR)"
        }
    ]
    questions.extend(d4)

    return questions

def get_questions_set2():
    # 65 distinct questions for Set 2
    questions = []
    
    # -------------------------------------------------------------
    # DOMAIN 1: CLOUD CONCEPTS (16 Questions: Q1 - Q16)
    # -------------------------------------------------------------
    d1 = [
        {
            "id": "aws-clf02-s2-001",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Scalability vs Elasticity)",
            "difficulty": "Medium",
            "question": "Which scenario best illustrates the concept of 'horizontal scalability' in cloud computing architecture?",
            "options": [
                "Adding more EC2 instances of equal size to an Auto Scaling group to distribute increased web traffic across a cluster",
                "Upgrading a single virtual server from a t3.medium instance type to an m5.4xlarge instance type",
                "Attaching a larger 2 TB EBS volume to an existing database server",
                "Increasing the maximum clock frequency of a physical CPU hyper-thread"
            ],
            "answer": 0,
            "explanation": "Horizontal scaling (scaling out) involves adding more compute instances to distribute the workload across a cluster (e.g., using an Auto Scaling group with an Application Load Balancer). Vertical scaling (scaling up) involves adding more CPU or RAM to an existing single instance.",
            "citation": "AWS Architecture Center — Horizontal vs Vertical Scaling"
        },
        {
            "id": "aws-clf02-s2-002",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (High Availability Architecture)",
            "difficulty": "Easy",
            "question": "How does distributing application servers across multiple Availability Zones in the same AWS Region enhance High Availability?",
            "options": [
                "It protects the application against single data center failure caused by localized power outages, fires, or hardware disruptions",
                "It eliminates all billing charges for inter-instance network data transfer",
                "It automatically converts relational database queries into non-relational graph queries",
                "It prevents users from connecting through unsecured public Wi-Fi networks"
            ],
            "answer": 0,
            "explanation": "Because Availability Zones are physically separated facilities with independent utility infrastructure, distributing servers across multiple AZs ensures that an event taking down one data center will not cause application downtime.",
            "citation": "AWS Global Infrastructure Guide — Multi-AZ Architecture"
        },
        {
            "id": "aws-clf02-s2-003",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Operational Excellence Pillar)",
            "difficulty": "Medium",
            "question": "Which design principle aligns directly with the Operational Excellence pillar of the AWS Well-Architected Framework?",
            "options": [
                "Perform operations as code and make frequent, small, reversible changes",
                "Deploy manual administrative console procedures to prevent automated script errors",
                "Avoid analyzing past production incidents to maintain forward engineering momentum",
                "Limit system telemetry metrics to save on logging storage costs"
            ],
            "answer": 0,
            "explanation": "The Operational Excellence pillar focuses on running and monitoring systems to deliver business value and continually improving processes. Key principles include performing operations as code, making frequent and reversible changes, and learning from all operational failures.",
            "citation": "AWS Well-Architected Framework — Operational Excellence Pillar"
        },
        {
            "id": "aws-clf02-s2-004",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Disaster Recovery Strategies)",
            "difficulty": "Hard",
            "question": "Which disaster recovery (DR) strategy involves maintaining a minimal, scaled-down version of core architecture running in a secondary AWS Region that can be rapidly scaled up if the primary region fails?",
            "options": [
                "Pilot Light",
                "Backup and Restore",
                "Warm Standby",
                "Multi-Region Active-Active"
            ],
            "answer": 0,
            "explanation": "In a Pilot Light DR strategy, the critical core elements of the workload (like continuous database replication) are kept running in the recovery region, while compute servers are powered off or scaled to zero until a failover event occurs, upon which they are quickly provisioned.",
            "citation": "AWS Disaster Recovery Whitepaper — Disaster Recovery Strategies"
        },
        {
            "id": "aws-clf02-s2-005",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (AWS Local Zones)",
            "difficulty": "Medium",
            "question": "Which AWS infrastructure deployment brings AWS compute, storage, and database services closer to large population, industry, and IT centers to deliver single-digit millisecond latency for real-time gaming and video rendering?",
            "options": [
                "AWS Local Zones",
                "AWS Snowball Edge",
                "AWS Direct Connect Locations",
                "Amazon S3 Transfer Acceleration Nodes"
            ],
            "answer": 0,
            "explanation": "AWS Local Zones place AWS compute, storage, database, and other select services closer to end-users in major metropolitan areas where no AWS Region currently exists, enabling sub-10 millisecond latency for demanding local workloads.",
            "citation": "AWS Local Zones Overview — Ultra-Low Latency Architecture"
        },
        {
            "id": "aws-clf02-s2-006",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (AWS Wavelength)",
            "difficulty": "Medium",
            "question": "Which infrastructure offering embeds AWS compute and storage services directly within telecommunication providers' 5G network data centers to deliver ultra-low latency applications for mobile devices and autonomous vehicles?",
            "options": [
                "AWS Wavelength",
                "AWS Outposts",
                "AWS Transit Gateway",
                "Amazon CloudFront Edge Locations"
            ],
            "answer": 0,
            "explanation": "AWS Wavelength optimizes applications for mobile devices by embedding AWS compute and storage services inside the 5G networks of telecom carriers, routing application traffic directly without leaving the mobile carrier's network.",
            "citation": "AWS Wavelength Developer Guide — 5G Edge Computing"
        },
        {
            "id": "aws-clf02-s2-007",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (AWS Outposts - On-Premises AWS)",
            "difficulty": "Medium",
            "question": "An enterprise requires certain workloads to remain physically on-premises in their local data center due to strict national data residency regulations, but wants to use the exact same AWS APIs, hardware, and management tools. Which service fulfills this?",
            "options": [
                "AWS Outposts",
                "AWS Storage Gateway",
                "AWS Direct Connect",
                "Amazon VPC Peering"
            ],
            "answer": 0,
            "explanation": "AWS Outposts brings native AWS services, infrastructure, and operating models directly to virtually any on-premises data center or co-location facility in a fully managed physical rack delivered and installed by AWS.",
            "citation": "AWS Outposts User Guide — Hybrid Cloud on-premises"
        },
        {
            "id": "aws-clf02-s2-008",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Performance Efficiency Pillar)",
            "difficulty": "Medium",
            "question": "Which design principle aligns with the Performance Efficiency pillar of the AWS Well-Architected Framework?",
            "options": [
                "Democratize advanced technologies by consuming them as managed services (e.g., machine learning, NoSQL databases) rather than building them from scratch",
                "Always run database instances on single-core virtual servers to keep resource consumption predictable",
                "Perform all operational testing only in production environments during peak traffic hours",
                "Restrict cloud storage to local hard drives attached to physical server racks"
            ],
            "answer": 0,
            "explanation": "The Performance Efficiency pillar emphasizes democratizing advanced technologies: technologies that require specialized expertise (such as media transcoding, NoSQL databases, or machine learning) should be consumed as managed services so your team can focus on development rather than resource management.",
            "citation": "AWS Well-Architected Framework — Performance Efficiency Pillar"
        },
        {
            "id": "aws-clf02-s2-009",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Cloud Benefit: Stop Guessing Capacity)",
            "difficulty": "Easy",
            "question": "How does the cloud eliminate the traditional risk of 'guessing capacity requirements' during product development?",
            "options": [
                "Workloads can scale up and scale out automatically in response to actual demand using services like EC2 Auto Scaling",
                "Customers are legally required to reserve static server quotas 12 months in advance",
                "AWS automatically charges a fixed flat monthly rate regardless of the number of servers created",
                "All applications are restricted to running on pre-allocated shared mainframe pools"
            ],
            "answer": 0,
            "explanation": "In traditional IT, organizations must estimate capacity before deployment, risking either underutilization (wasted money) or under-provisioning (outages). With cloud elasticity and Auto Scaling, capacity scales dynamically with live demand.",
            "citation": "AWS Cloud Practitioner Essentials — Advantages of Cloud Computing"
        },
        {
            "id": "aws-clf02-s2-010",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Disaster Recovery RTO and RPO)",
            "difficulty": "Hard",
            "question": "In disaster recovery planning, what does the Recovery Time Objective (RTO) represent?",
            "options": [
                "The maximum acceptable duration of time that an application can be offline following an outage",
                "The maximum acceptable amount of data loss measured in time between backup points",
                "The total financial cost incurred during a cloud migration assessment",
                "The time required to provision a brand-new AWS root administrative account"
            ],
            "answer": 0,
            "explanation": "Recovery Time Objective (RTO) is the maximum acceptable time an application can be unavailable before normal service is restored. Recovery Point Objective (RPO) is the maximum acceptable period of data loss measured backward in time.",
            "citation": "AWS Disaster Recovery Whitepaper — RTO and RPO Metrics"
        },
        {
            "id": "aws-clf02-s2-011",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Microservices vs Monolithic Architecture)",
            "difficulty": "Medium",
            "question": "Why is a microservices architecture preferred over a monolithic architecture when building highly resilient cloud applications?",
            "options": [
                "Microservices decouple components so that failures in one service do not cascade and bring down the entire application",
                "Microservices require all code to be written in a single unified programming language",
                "Microservices store all user session state inside a single relational database table",
                "Microservices eliminate the need for container orchestrators and network APIs"
            ],
            "answer": 0,
            "explanation": "A microservices architecture breaks complex applications into smaller, independent components that communicate via APIs or message queues. If one service experiences a disruption, other services continue operating without cascading system failure.",
            "citation": "AWS Architecture Center — Microservices Architecture on AWS"
        },
        {
            "id": "aws-clf02-s2-012",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (PaaS Benefits)",
            "difficulty": "Easy",
            "question": "Which statement accurately describes a major advantage of Platform as a Service (PaaS) offerings like AWS Elastic Beanstalk?",
            "options": [
                "Customers can focus entirely on writing application code while the cloud provider manages server provisioning, OS patches, and auto-scaling",
                "Customers have full physical access to the server motherboards in AWS data center facilities",
                "Customers are required to manually install kernel security updates on hypervisors every 30 days",
                "PaaS applications can only communicate with on-premises mainframe servers"
            ],
            "answer": 0,
            "explanation": "Platform as a Service (PaaS) removes the need for organizations to manage underlying hardware and operating systems. Developers focus purely on deployment and management of their applications.",
            "citation": "AWS Cloud Practitioner Essentials — Types of Cloud Computing"
        },
        {
            "id": "aws-clf02-s2-013",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (AWS Well-Architected Tool)",
            "difficulty": "Medium",
            "question": "Which self-service tool in the AWS Management Console enables architects to review their state of workloads against the AWS Well-Architected Framework and provides actionable remediation guidance?",
            "options": [
                "AWS Well-Architected Tool",
                "AWS Trusted Advisor",
                "AWS Compute Optimizer",
                "AWS Service Catalog"
            ],
            "answer": 0,
            "explanation": "The AWS Well-Architected Tool is a free service that provides a consistent process for evaluating architectures against Well-Architected pillars, identifying high- and medium-risk issues, and providing improvement roadmaps.",
            "citation": "AWS Well-Architected Tool User Guide"
        },
        {
            "id": "aws-clf02-s2-014",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Multi-Region Active-Active Strategy)",
            "difficulty": "Hard",
            "question": "Which disaster recovery strategy achieves the lowest possible Recovery Time Objective (RTO) and Recovery Point Objective (RPO) by serving user traffic simultaneously from two or more AWS Regions?",
            "options": [
                "Multi-Region Active-Active",
                "Warm Standby",
                "Pilot Light",
                "Backup and Restore"
            ],
            "answer": 0,
            "explanation": "A Multi-Region Active-Active strategy deploys full application stacks and synchronously/near-synchronously replicates data across two or more AWS Regions. User requests are routed to the nearest healthy region, achieving near-zero RTO and RPO.",
            "citation": "AWS Disaster Recovery Whitepaper — Multi-Region Strategies"
        },
        {
            "id": "aws-clf02-s2-015",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (Cloud Economics: Trade Fixed for Variable)",
            "difficulty": "Easy",
            "question": "What is the primary financial risk eliminated when an enterprise replaces heavy on-premises server purchasing with AWS pay-as-you-go pricing?",
            "options": [
                "The risk of investing large amounts of capital in hardware that becomes idle or insufficient as business needs shift",
                "The risk of receiving automated electronic monthly invoices from cloud vendors",
                "The risk of application response times improving beyond user expectations",
                "The risk of having too many automated data backups stored across multiple Availability Zones"
            ],
            "answer": 0,
            "explanation": "Trading fixed capital expenses for variable expenses eliminates the risk of purchasing expensive physical servers that sit idle during demand troughs or become a bottleneck during unexpected growth spikes.",
            "citation": "AWS Cloud Value Framework — Eliminating Capital Waste"
        },
        {
            "id": "aws-clf02-s2-016",
            "type": "mcq",
            "subtopic": "Domain 1: Cloud Concepts (SaaS Examples)",
            "difficulty": "Easy",
            "question": "Which of the following is considered a Software as a Service (SaaS) solution on AWS?",
            "options": [
                "Amazon QuickSight",
                "Amazon EC2 bare-metal instances",
                "Amazon Virtual Private Cloud (VPC)",
                "Amazon Elastic Block Store (EBS) standard volumes"
            ],
            "answer": 0,
            "explanation": "Software as a Service (SaaS) provides complete, fully managed applications that users consume over the web without managing any underlying infrastructure or platform code. Amazon QuickSight (business intelligence) is an example of a SaaS product on AWS.",
            "citation": "AWS Cloud Practitioner Essentials — Cloud Service Categories"
        }
    ]
    questions.extend(d1)

    # -------------------------------------------------------------
    # DOMAIN 2: SECURITY & COMPLIANCE (20 Questions: Q17 - Q36)
    # -------------------------------------------------------------
    d2 = [
        {
            "id": "aws-clf02-s2-017",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Shared Responsibility for S3)",
            "difficulty": "Medium",
            "question": "When storing corporate data in an Amazon S3 bucket, which security responsibility falls squarely on the customer according to the AWS Shared Responsibility Model?",
            "options": [
                "Configuring bucket access policies, IAM user permissions, and enabling server-side encryption",
                "Maintaining the physical storage drives and disk firmware inside the S3 storage arrays",
                "Ensuring regional power grid redundancy for the data center housing the S3 disks",
                "Managing multi-AZ storage replication protocols in the underlying storage cluster"
            ],
            "answer": 0,
            "explanation": "Under the Shared Responsibility Model, AWS manages the physical storage infrastructure, drive decommissioning, and cluster hardware. The customer is responsible for managing S3 bucket permissions, public access blocks, and configuring encryption settings.",
            "citation": "Amazon S3 Security Guide — Customer Responsibilities"
        },
        {
            "id": "aws-clf02-s2-018",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS IAM Password Policy)",
            "difficulty": "Easy",
            "question": "Which AWS IAM feature allows administrators to mandate minimum password lengths, require specific character combinations, and enforce periodic password expirations for IAM users?",
            "options": [
                "IAM Account Password Policy",
                "Service Control Policy (SCP)",
                "Security Group Inbound Rule",
                "Amazon Cognito User Pool Rule"
            ],
            "answer": 0,
            "explanation": "Administrators can configure an IAM Account Password Policy in the IAM console to enforce password complexity rules, minimum character lengths, prevent password reuse, and mandate regular password rotations.",
            "citation": "AWS IAM User Guide — Managing Account Password Policies"
        },
        {
            "id": "aws-clf02-s2-019",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS IAM Access Analyzer)",
            "difficulty": "Medium",
            "question": "Which IAM feature analyzes resource-based policies across S3 buckets, KMS keys, and IAM roles to alert administrators if resources are accessible from outside their AWS account or organization?",
            "options": [
                "IAM Access Analyzer",
                "AWS Systems Manager Inventory",
                "Amazon Inspector",
                "AWS Trusted Advisor Cost Filter"
            ],
            "answer": 0,
            "explanation": "IAM Access Analyzer uses mathematical logic and provable security to analyze resource-based policies and generate findings when resources (like S3 buckets or KMS keys) are shared with public or external identities outside the organization.",
            "citation": "AWS IAM User Guide — Identifying External Access with Access Analyzer"
        },
        {
            "id": "aws-clf02-s2-020",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS CloudHSM vs AWS KMS)",
            "difficulty": "Hard",
            "question": "An enterprise must comply with strict corporate mandates requiring dedicated, FIPS 140-2 Level 3 validated single-tenant hardware security modules where only the customer controls the encryption keys and hardware partition. Which service satisfies this requirement?",
            "options": [
                "AWS CloudHSM",
                "AWS Key Management Service (AWS KMS) Standard",
                "AWS Secrets Manager",
                "AWS Certificate Manager"
            ],
            "answer": 0,
            "explanation": "AWS CloudHSM provides dedicated, single-tenant physical Hardware Security Module (HSM) appliances directly within the customer's VPC. Unlike AWS KMS (which is a multi-tenant managed service), CloudHSM gives customers sole cryptographic control over HSM hardware partitions.",
            "citation": "AWS CloudHSM User Guide — Dedicated HSM Architecture"
        },
        {
            "id": "aws-clf02-s2-021",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Certificate Manager - ACM)",
            "difficulty": "Easy",
            "question": "Which service allows customers to provision, manage, and deploy public Secure Sockets Layer / Transport Layer Security (SSL/TLS) certificates for use with Elastic Load Balancers and Amazon CloudFront distributions with free automated renewal?",
            "options": [
                "AWS Certificate Manager (ACM)",
                "AWS Key Management Service (AWS KMS)",
                "AWS IAM Credential Manager",
                "Amazon Route 53 Resolver"
            ],
            "answer": 0,
            "explanation": "AWS Certificate Manager (ACM) makes it easy to provision, manage, and deploy public and private SSL/TLS certificates for use with integrated AWS services like Elastic Load Balancing, CloudFront, and API Gateway, featuring free automated certificate renewal.",
            "citation": "AWS Certificate Manager User Guide — Overview of ACM"
        },
        {
            "id": "aws-clf02-s2-022",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Amazon Security Lake)",
            "difficulty": "Medium",
            "question": "Which service automatically centralizes, normalizes, and manages security log data from multiple AWS accounts, VPC Flow Logs, and third-party security vendors into the Open Cybersecurity Schema Framework (OCSF) format?",
            "options": [
                "Amazon Security Lake",
                "Amazon GuardDuty",
                "AWS CloudTrail Insights",
                "Amazon Detective"
            ],
            "answer": 0,
            "explanation": "Amazon Security Lake automatically centralizes security data from cloud, on-premises, and custom sources into a purpose-built security data lake, normalizing logs into the OCSF standard for rapid multi-account security analysis.",
            "citation": "Amazon Security Lake Documentation — Centralized Log Lake"
        },
        {
            "id": "aws-clf02-s2-023",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Amazon Detective - Investigation)",
            "difficulty": "Medium",
            "question": "Following an alert from Amazon GuardDuty regarding suspicious account activity, which AWS service helps security teams analyze, investigate, and quickly identify the root cause of potential security issues using interactive graph visualizations?",
            "options": [
                "Amazon Detective",
                "AWS X-Ray",
                "AWS Audit Manager",
                "AWS Systems Manager Run Command"
            ],
            "answer": 0,
            "explanation": "Amazon Detective automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked dataset that enables rapid investigation of security findings from GuardDuty.",
            "citation": "Amazon Detective Administration Guide — Root Cause Investigation"
        },
        {
            "id": "aws-clf02-s2-024",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Security Hub - CSPM)",
            "difficulty": "Medium",
            "question": "Which service acts as a single pane of glass for Cloud Security Posture Management (CSPM), aggregating security findings from GuardDuty, Inspector, Macie, and IAM Access Analyzer against CIS AWS Foundations benchmarks?",
            "options": [
                "AWS Security Hub",
                "AWS Trusted Advisor",
                "AWS Systems Manager Explorer",
                "AWS Control Tower"
            ],
            "answer": 0,
            "explanation": "AWS Security Hub gives you a comprehensive view of your security state across all AWS accounts. It aggregates, organizes, and prioritizes security alerts and findings from multiple AWS services and checks environments against compliance standards like CIS and PCI DSS.",
            "citation": "AWS Security Hub User Guide — Aggregating Security Findings"
        },
        {
            "id": "aws-clf02-s2-025",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Control Tower - Landing Zones)",
            "difficulty": "Medium",
            "question": "An enterprise wants to establish a well-architected, secure multi-account AWS environment using automated organizational units, preventive guardrails, and centralized identity federation. Which service automates this setup?",
            "options": [
                "AWS Control Tower",
                "AWS Direct Connect",
                "Amazon CloudWatch Synthetics",
                "AWS Elastic Beanstalk"
            ],
            "answer": 0,
            "explanation": "AWS Control Tower provides the easiest way to set up and govern a secure, multi-account AWS environment (called a landing zone) based on best-practice blueprints and automated guardrails.",
            "citation": "AWS Control Tower User Guide — Establishing Landing Zones"
        },
        {
            "id": "aws-clf02-s2-026",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Network Firewall)",
            "difficulty": "Hard",
            "question": "Which stateful network security service provides high-throughput Layer 3 through Layer 7 stateful packet inspection, URL domain filtering, and intrusion prevention system (IPS) capabilities for entire Amazon VPCs?",
            "options": [
                "AWS Network Firewall",
                "Security Groups",
                "Network ACLs",
                "AWS WAF"
            ],
            "answer": 0,
            "explanation": "AWS Network Firewall is a managed service that deploys stateful Layer 3-7 inspection across VPC boundaries. Unlike Security Groups or NACLs, it includes advanced intrusion prevention rules (Suricata-compatible) and outbound domain filtering.",
            "citation": "AWS Network Firewall Developer Guide — Stateful Traffic Inspection"
        },
        {
            "id": "aws-clf02-s2-027",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (IAM Policy Structure)",
            "difficulty": "Medium",
            "question": "In an AWS IAM JSON policy document, what are the four fundamental building-block elements that define the access grant or restriction?",
            "options": [
                "Effect, Action, Resource, and Condition",
                "Protocol, Port, Subnet, and Direction",
                "Domain, URL, Method, and Headers",
                "Instance, Disk, Volume, and Snapshot"
            ],
            "answer": 0,
            "explanation": "An IAM policy statement consists of four core elements: Effect (Allow or Deny), Action (the specific API operations, like s3:GetObject), Resource (the ARN of the target resource), and optional Condition (rules under which the policy applies).",
            "citation": "AWS IAM User Guide — Grammar of the IAM Policy Language"
        },
        {
            "id": "aws-clf02-s2-028",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (DDoS Mitigation with CloudFront)",
            "difficulty": "Medium",
            "question": "How does deploying Amazon CloudFront in front of web applications improve overall DDoS attack resilience?",
            "options": [
                "By absorbing attack traffic across hundreds of globally distributed edge locations, shielding the origin server from direct traffic spikes",
                "By automatically deleting the origin web server when an attack is detected",
                "By requiring all end-users to enter biometric identity authentication before loading web pages",
                "By disabling all HTTP POST requests across the entire application"
            ],
            "answer": 0,
            "explanation": "Amazon CloudFront is integrated with AWS Shield Standard. Because CloudFront terminates connections at edge locations worldwide, it absorbs and diffuses massive Layer 3/4 volumetric DDoS attacks, keeping the backend origin servers protected.",
            "citation": "AWS Best Practices for DDoS Resiliency — Edge Architecture"
        },
        {
            "id": "aws-clf02-s2-029",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Audit Manager)",
            "difficulty": "Medium",
            "question": "Which compliance service helps teams continuously map their AWS resource usage to industry compliance frameworks (such as GDPR, HIPAA, and PCI DSS) while automatically collecting regulatory evidence?",
            "options": [
                "AWS Audit Manager",
                "AWS Artifact",
                "Amazon GuardDuty",
                "AWS Config Rules Engine"
            ],
            "answer": 0,
            "explanation": "AWS Audit Manager helps continuously audit your AWS usage to simplify risk assessment and compliance with industry standards. It automates evidence collection to streamline external audits.",
            "citation": "AWS Audit Manager User Guide — Continuous Compliance Auditing"
        },
        {
            "id": "aws-clf02-s2-030",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS IAM Identity Center - SSO)",
            "difficulty": "Medium",
            "question": "Which service provides a centralized portal where workforce users can sign in once (SSO) to access all their assigned AWS accounts and third-party SaaS cloud applications (such as Microsoft 365)?",
            "options": [
                "AWS IAM Identity Center (successor to AWS Single Sign-On)",
                "Amazon Cognito Identity Pools",
                "AWS Directory Service Connector",
                "AWS Organizations Master Vault"
            ],
            "answer": 0,
            "explanation": "AWS IAM Identity Center (formerly AWS SSO) is the recommended service for managing workforce access to AWS accounts and cloud business applications. It connects with your existing identity provider (like Active Directory or Okta).",
            "citation": "AWS IAM Identity Center User Guide — Workforce Identity Management"
        },
        {
            "id": "aws-clf02-s2-031",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Amazon S3 Block Public Access)",
            "difficulty": "Easy",
            "question": "Which Amazon S3 feature provides centralized settings at the account or bucket level that override all bucket policies and access control lists to guarantee that S3 buckets cannot be made public?",
            "options": [
                "Amazon S3 Block Public Access",
                "Amazon S3 Object Lock",
                "Amazon S3 Versioning",
                "Amazon S3 Server-Side Encryption (SSE-S3)"
            ],
            "answer": 0,
            "explanation": "Amazon S3 Block Public Access settings provide controls across an entire AWS account or individual buckets to ensure objects cannot become publicly accessible, preventing accidental data leaks.",
            "citation": "Amazon S3 User Guide — Blocking Public Access"
        },
        {
            "id": "aws-clf02-s2-032",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Hardware Decommissioning at AWS)",
            "difficulty": "Easy",
            "question": "According to the AWS Shared Responsibility Model, who is responsible for the secure physical destruction and decommissioning of decommissioned hard drives that formerly stored customer data?",
            "options": [
                "AWS, following rigorous Department of Defense (DoD 5220.22-M) and NIST 800-88 sanitization standards",
                "The customer, who must send physical technicians to AWS data centers to oversee disk shredding",
                "Local municipal government recycling authorities",
                "Third-party commercial electronics salvage wholesalers"
            ],
            "answer": 0,
            "explanation": "AWS is responsible for the physical security of data center hardware. When storage devices reach the end of their useful life, AWS decommissions and destroys them in accordance with NIST 800-88 sanitization techniques.",
            "citation": "AWS Data Center Physical Security Overview — Media Sanitization"
        },
        {
            "id": "aws-clf02-s2-033",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS Systems Manager Parameter Store)",
            "difficulty": "Medium",
            "question": "Which capability of AWS Systems Manager provides secure, hierarchical storage for configuration data (such as database connection strings, passwords, and license codes) with support for KMS encryption?",
            "options": [
                "Parameter Store",
                "Run Command",
                "Session Manager",
                "Patch Manager"
            ],
            "answer": 0,
            "explanation": "AWS Systems Manager Parameter Store provides secure, hierarchical storage for configuration data management and secrets management. You can store values as plain text or encrypted strings using AWS KMS.",
            "citation": "AWS Systems Manager User Guide — Parameter Store Overview"
        },
        {
            "id": "aws-clf02-s2-034",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (AWS CloudTrail Lake)",
            "difficulty": "Hard",
            "question": "Which managed audit tool allows security teams to run SQL-based analytical queries directly on immutable CloudTrail activity logs without having to export them into external databases?",
            "options": [
                "AWS CloudTrail Lake",
                "Amazon CloudWatch Insights",
                "Amazon Athena Standard Tables",
                "AWS Glue Data Catalog"
            ],
            "answer": 0,
            "explanation": "CloudTrail Lake is a managed security and audit data lake that aggregates, immutably stores, and enables SQL queries on user and API activity recorded by CloudTrail without requiring complex ETL pipelines.",
            "citation": "AWS CloudTrail User Guide — Working with CloudTrail Lake"
        },
        {
            "id": "aws-clf02-s2-035",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Shared Responsibility: Guest OS vs Hypervisor)",
            "difficulty": "Medium",
            "question": "In an Infrastructure as a Service (IaaS) deployment using Amazon EC2, who is responsible for applying security patches to the physical hypervisor that hosts virtual instances?",
            "options": [
                "AWS is responsible for patching the physical hypervisor",
                "The customer is responsible for patching the physical hypervisor",
                "Both AWS and the customer must coordinate simultaneous hypervisor restarts",
                "The operating system vendor (e.g., Microsoft or Canonical) is responsible"
            ],
            "answer": 0,
            "explanation": "Under the Shared Responsibility Model, AWS owns the virtualization layer (hypervisor) and the physical host server. The customer has zero access to the underlying hypervisor and is only responsible for the guest OS inside their virtual instance.",
            "citation": "AWS Shared Responsibility Model Documentation — Hypervisor Layer"
        },
        {
            "id": "aws-clf02-s2-036",
            "type": "mcq",
            "subtopic": "Domain 2: Security & Compliance (Multi-Factor Authentication Methods)",
            "difficulty": "Easy",
            "question": "Which authentication factor options can be used to enable Multi-Factor Authentication (MFA) on an AWS IAM user account?",
            "options": [
                "FIDO-certified security keys (e.g., YubiKey) and virtual authenticator apps (e.g., Google Authenticator)",
                "Standard unencrypted email links and plain text SMS password reminders",
                "Credit card verification numbers stored in browser cookies",
                "Static challenge questions based on childhood pet names"
            ],
            "answer": 0,
            "explanation": "AWS supports multiple MFA methods for IAM users, including FIDO-certified physical hardware keys (YubiKey), virtual MFA authenticator apps (Google Authenticator, Microsoft Authenticator), and hardware TOTP tokens.",
            "citation": "AWS IAM User Guide — Supported MFA Device Types"
        }
    ]
    questions.extend(d2)

    # -------------------------------------------------------------
    # DOMAIN 3: CLOUD TECHNOLOGY & SERVICES (22 Questions: Q37 - Q58)
    # -------------------------------------------------------------
    d3 = [
        {
            "id": "aws-clf02-s2-037",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (EC2 Instance Types)",
            "difficulty": "Easy",
            "question": "Which Amazon EC2 instance family is specifically optimized for memory-intensive workloads such as in-memory databases (Redis/Memcached), distributed memory caches, and high-performance relational databases?",
            "options": [
                "Memory Optimized (e.g., R-family)",
                "Compute Optimized (e.g., C-family)",
                "Storage Optimized (e.g., I-family)",
                "Accelerated Computing (e.g., P-family)"
            ],
            "answer": 0,
            "explanation": "Memory Optimized instances (such as R-family instances) are engineered to deliver fast performance for workloads that process large data sets in memory (such as high-performance databases and real-time distributed caches).",
            "citation": "Amazon EC2 Instance Types Guide — Memory Optimized"
        },
        {
            "id": "aws-clf02-s2-038",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS Fargate - Serverless Containers)",
            "difficulty": "Medium",
            "question": "Which serverless compute engine allows teams to run Docker containers on Amazon ECS or Amazon EKS without having to provision, configure, or scale underlying EC2 virtual servers?",
            "options": [
                "AWS Fargate",
                "Amazon EC2 Dedicated Hosts",
                "AWS Batch Bare Metal",
                "Amazon Elastic Beanstalk Worker Tier"
            ],
            "answer": 0,
            "explanation": "AWS Fargate is a serverless, pay-as-you-go compute engine that lets you build applications without managing servers. Fargate runs containers on Amazon ECS and Amazon EKS without requiring you to manage EC2 clusters.",
            "citation": "AWS Fargate User Guide — Serverless Container Compute"
        },
        {
            "id": "aws-clf02-s2-039",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon S3 Glacier Flexible Retrieval vs Deep Archive)",
            "difficulty": "Medium",
            "question": "An enterprise must store compliance archives for 10 years that are accessed only once or twice per year, where a retrieval time of 12 hours is completely acceptable. Which S3 storage class offers the lowest storage cost in the AWS Cloud?",
            "options": [
                "S3 Glacier Deep Archive",
                "S3 Glacier Flexible Retrieval",
                "S3 Standard-Infrequent Access",
                "S3 Intelligent-Tiering Archive Instant"
            ],
            "answer": 0,
            "explanation": "S3 Glacier Deep Archive is Amazon S3's lowest-cost storage class, designed for long-term retention of data that is accessed rarely (1-2 times a year) and where retrieval times of 12 to 48 hours are acceptable.",
            "citation": "Amazon S3 Storage Classes — S3 Glacier Deep Archive"
        },
        {
            "id": "aws-clf02-s2-040",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon EBS Volume Types)",
            "difficulty": "Medium",
            "question": "Which Amazon EBS volume type is designed as the default cost-effective storage option for a broad range of transactional workloads, virtual desktops, and medium-sized databases?",
            "options": [
                "General Purpose SSD (gp3)",
                "Provisioned IOPS SSD (io2)",
                "Throughput Optimized HDD (st1)",
                "Cold HDD (sc1)"
            ],
            "answer": 0,
            "explanation": "General Purpose SSD (gp3) volumes offer the ideal balance of price and performance for a wide range of transactional applications, boot volumes, and dev/test environments, allowing independent IOPS and throughput provisioning.",
            "citation": "Amazon EBS Volume Types Documentation — General Purpose SSD"
        },
        {
            "id": "aws-clf02-s2-041",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS Storage Gateway - Hybrid File/Volume/Tape)",
            "difficulty": "Hard",
            "question": "Which hybrid storage service allows on-premises applications to seamlessly connect to virtually unlimited cloud storage in Amazon S3 over standard storage protocols (such as NFS, SMB, and iSCSI)?",
            "options": [
                "AWS Storage Gateway",
                "AWS Direct Connect",
                "Amazon EFS Mount Target",
                "AWS Snowball Edge"
            ],
            "answer": 0,
            "explanation": "AWS Storage Gateway is a hybrid cloud storage service that connects on-premises environments with AWS storage (S3, EBS, Glacier). It provides File Gateway (NFS/SMB), Volume Gateway (iSCSI), and Tape Gateway (virtual tape library).",
            "citation": "AWS Storage Gateway User Guide — Hybrid Architecture"
        },
        {
            "id": "aws-clf02-s2-042",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon EC2 Auto Scaling)",
            "difficulty": "Easy",
            "question": "What is the primary function of Amazon EC2 Auto Scaling?",
            "options": [
                "To automatically adjust the number of active EC2 instances up or down based on traffic demand and health checks",
                "To automatically convert SQL queries into NoSQL JSON documents",
                "To reboot all customer virtual instances every night at midnight",
                "To automatically negotiate lower domain name renewal fees"
            ],
            "answer": 0,
            "explanation": "Amazon EC2 Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost, launching instances when traffic surges and terminating them when demand drops.",
            "citation": "Amazon EC2 Auto Scaling User Guide — Overview"
        },
        {
            "id": "aws-clf02-s2-043",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Elastic Load Balancing - ALB vs NLB)",
            "difficulty": "Medium",
            "question": "An architect needs to route web requests based on the URL path (e.g., routing /orders to one container fleet and /images to another) at Layer 7. Which load balancer should be chosen?",
            "options": [
                "Application Load Balancer (ALB)",
                "Network Load Balancer (NLB)",
                "Gateway Load Balancer (GWLB)",
                "Classic Load Balancer (CLB)"
            ],
            "answer": 0,
            "explanation": "Application Load Balancer (ALB) operates at the request level (Layer 7) and supports advanced routing features, such as path-based routing, host-based routing, and routing to containerized applications.",
            "citation": "Elastic Load Balancing User Guide — Application Load Balancers"
        },
        {
            "id": "aws-clf02-s2-044",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Network Load Balancer - Ultra Low Latency)",
            "difficulty": "Medium",
            "question": "Which Elastic Load Balancer operates at Layer 4 (Transport layer) and is capable of handling millions of requests per second with ultra-low latency while supporting static IP addresses?",
            "options": [
                "Network Load Balancer (NLB)",
                "Application Load Balancer (ALB)",
                "Gateway Load Balancer (GWLB)",
                "Amazon Route 53 Traffic Flow"
            ],
            "answer": 0,
            "explanation": "Network Load Balancer (NLB) operates at the connection level (Layer 4) and is optimized to handle volatile traffic patterns and millions of requests per second with ultra-low latency. It provides a static IP per Availability Zone.",
            "citation": "Elastic Load Balancing User Guide — Network Load Balancer"
        },
        {
            "id": "aws-clf02-s2-045",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon Transit Gateway)",
            "difficulty": "Medium",
            "question": "Which networking service acts as a centralized regional cloud router, simplifying network topology by connecting thousands of Amazon VPCs and on-premises networks through a central hub rather than complex mesh peering?",
            "options": [
                "AWS Transit Gateway",
                "AWS Direct Connect Gateway",
                "Amazon VPC Peering Mesh",
                "Internet Gateway"
            ],
            "answer": 0,
            "explanation": "AWS Transit Gateway connects Amazon VPCs and on-premises networks through a central hub. This hub-and-spoke model eliminates the need for complex, unmanageable point-to-point VPC peering connections across enterprise environments.",
            "citation": "AWS Transit Gateway Guide — Centralized Network Routing"
        },
        {
            "id": "aws-clf02-s2-046",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon EventBridge - Event Bus)",
            "difficulty": "Medium",
            "question": "Which serverless service makes it easy to connect applications together using real-time data streams from SaaS applications, custom applications, and AWS services using an event-driven architecture?",
            "options": [
                "Amazon EventBridge",
                "Amazon SQS",
                "AWS Step Functions",
                "AWS Glue"
            ],
            "answer": 0,
            "explanation": "Amazon EventBridge is a serverless event bus service that makes it easy to connect applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your applications, third-party SaaS apps, and AWS services.",
            "citation": "Amazon EventBridge User Guide — Event-Driven Architecture"
        },
        {
            "id": "aws-clf02-s2-047",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS Step Functions - Workflow Orchestration)",
            "difficulty": "Medium",
            "question": "Which visual workflow orchestration service allows developers to coordinate multiple AWS Lambda functions and microservices into state machines with built-in error handling and retries?",
            "options": [
                "AWS Step Functions",
                "Amazon EventBridge",
                "AWS CodePipeline",
                "AWS Systems Manager Run Command"
            ],
            "answer": 0,
            "explanation": "AWS Step Functions is a low-code visual workflow service used to orchestrate AWS services, automate business processes, and build distributed applications using finite state machines.",
            "citation": "AWS Step Functions Developer Guide — Visual Workflows"
        },
        {
            "id": "aws-clf02-s2-048",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon OpenSearch Service)",
            "difficulty": "Easy",
            "question": "Which managed AWS service makes it easy to perform interactive log analytics, real-time application monitoring, and full-text search across application data using open-source OpenSearch or Elasticsearch engines?",
            "options": [
                "Amazon OpenSearch Service",
                "Amazon Athena",
                "Amazon Kinesis Data Streams",
                "Amazon QuickSight"
            ],
            "answer": 0,
            "explanation": "Amazon OpenSearch Service is a fully managed service that makes it easy to deploy, operate, and scale OpenSearch clusters for application search, website search, and real-time log analytics.",
            "citation": "Amazon OpenSearch Service Developer Guide"
        },
        {
            "id": "aws-clf02-s2-049",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon Athena - Serverless SQL on S3)",
            "difficulty": "Easy",
            "question": "Which serverless interactive query service allows data analysts to analyze data stored in Amazon S3 directly using standard SQL queries, paying only for the queries they run without loading data into a database?",
            "options": [
                "Amazon Athena",
                "Amazon Redshift",
                "Amazon RDS",
                "Amazon DocumentDB"
            ],
            "answer": 0,
            "explanation": "Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.",
            "citation": "Amazon Athena User Guide — Serverless SQL Queries on S3"
        },
        {
            "id": "aws-clf02-s2-050",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon EMR - Big Data Processing)",
            "difficulty": "Medium",
            "question": "Which managed cloud big data platform enables data engineers to run large-scale distributed data processing frameworks like Apache Spark, Apache Hadoop, and Presto on AWS?",
            "options": [
                "Amazon EMR (Elastic MapReduce)",
                "AWS Glue",
                "Amazon Kinesis",
                "Amazon QuickSight"
            ],
            "answer": 0,
            "explanation": "Amazon EMR is an industry-leading cloud big data platform for processing vast amounts of data using open-source tools such as Apache Spark, Apache Hive, Apache HBase, Presto, and Hadoop.",
            "citation": "Amazon EMR Management Guide — Big Data Frameworks"
        },
        {
            "id": "aws-clf02-s2-051",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS Glue - Serverless ETL)",
            "difficulty": "Medium",
            "question": "Which serverless data integration service discovers, categorizes, cleans, transforms, and loads (ETL) data from diverse sources into data lakes or data warehouses, featuring an automated metadata Data Catalog?",
            "options": [
                "AWS Glue",
                "Amazon EMR",
                "AWS DataSync",
                "AWS Database Migration Service (DMS)"
            ],
            "answer": 0,
            "explanation": "AWS Glue is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development with an integrated AWS Glue Data Catalog.",
            "citation": "AWS Glue Developer Guide — Serverless ETL Pipelines"
        },
        {
            "id": "aws-clf02-s2-052",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS DMS - Database Migration Service)",
            "difficulty": "Medium",
            "question": "Which service helps businesses migrate relational databases, non-relational databases, and data warehouses to AWS securely with minimal downtime, keeping the source database fully operational during migration?",
            "options": [
                "AWS Database Migration Service (AWS DMS)",
                "AWS DataSync",
                "AWS Application Migration Service (MGN)",
                "AWS Snowball Edge"
            ],
            "answer": 0,
            "explanation": "AWS Database Migration Service (AWS DMS) helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database.",
            "citation": "AWS Database Migration Service User Guide"
        },
        {
            "id": "aws-clf02-s2-053",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon SageMaker - Fully Managed ML)",
            "difficulty": "Easy",
            "question": "Which fully managed machine learning service provides developers and data scientists with all the tools needed to build, train, tune, and deploy machine learning models quickly into production?",
            "options": [
                "Amazon SageMaker",
                "Amazon Rekognition",
                "Amazon Polly",
                "Amazon Comprehend"
            ],
            "answer": 0,
            "explanation": "Amazon SageMaker is a fully managed service that brings together a broad set of tools for building, training, tuning, and deploying machine learning models at scale, including pre-built algorithms and one-click deployment.",
            "citation": "Amazon SageMaker Developer Guide — Machine Learning at Scale"
        },
        {
            "id": "aws-clf02-s2-054",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AI Services: Rekognition / Polly / Transcribe)",
            "difficulty": "Easy",
            "question": "A developer needs to convert written blog articles into lifelike, natural-sounding spoken audio speech files. Which pre-trained AWS AI service performs text-to-speech conversion?",
            "options": [
                "Amazon Polly",
                "Amazon Transcribe",
                "Amazon Rekognition",
                "Amazon Lex"
            ],
            "answer": 0,
            "explanation": "Amazon Polly is a cloud service that turns text into lifelike speech using advanced deep learning technologies to synthesize natural sounding human speech across dozens of languages.",
            "citation": "Amazon Polly Developer Guide — Text-to-Speech"
        },
        {
            "id": "aws-clf02-s2-055",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon Lex - Conversational AI)",
            "difficulty": "Easy",
            "question": "Which managed AI service provides advanced natural language understanding and automatic speech recognition to build conversational interfaces and voice chatbots into applications (powering Amazon Alexa)?",
            "options": [
                "Amazon Lex",
                "Amazon Kendra",
                "Amazon Textract",
                "Amazon Translate"
            ],
            "answer": 0,
            "explanation": "Amazon Lex is a fully managed service that provides advanced natural language understanding (NLU) and automatic speech recognition (ASR) to build conversational interfaces (chatbots) into any application.",
            "citation": "Amazon Lex Developer Guide — Building Conversational Chatbots"
        },
        {
            "id": "aws-clf02-s2-056",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS Global Accelerator)",
            "difficulty": "Medium",
            "question": "Which networking service uses the AWS global private network to optimize the path from end users to applications, providing static anycast IP addresses and improving TCP/UDP performance by up to 60%?",
            "options": [
                "AWS Global Accelerator",
                "Amazon Route 53",
                "Amazon CloudFront",
                "AWS Direct Connect"
            ],
            "answer": 0,
            "explanation": "AWS Global Accelerator is a networking service that improves the availability and performance of applications by routing traffic over the AWS global network infrastructure using static Anycast IP addresses.",
            "citation": "AWS Global Accelerator Developer Guide"
        },
        {
            "id": "aws-clf02-s2-057",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (Amazon VPC Endpoints / PrivateLink)",
            "difficulty": "Hard",
            "question": "How can EC2 instances in a private subnet access Amazon S3 buckets without traversing the public internet or requiring an Internet Gateway / NAT Gateway?",
            "options": [
                "By creating a VPC Gateway Endpoint for Amazon S3 in the VPC route table",
                "By assigning public Elastic IP addresses to all private EC2 instances",
                "By establishing an SSH tunnel through an external bastion host",
                "By enabling S3 Transfer Acceleration on the target bucket"
            ],
            "answer": 0,
            "explanation": "VPC Gateway Endpoints for Amazon S3 allow instances in private subnets to communicate directly with Amazon S3 over private AWS network routes without sending traffic over the public internet, requiring zero NAT devices.",
            "citation": "Amazon VPC User Guide — Gateway VPC Endpoints for Amazon S3"
        },
        {
            "id": "aws-clf02-s2-058",
            "type": "mcq",
            "subtopic": "Domain 3: Technology & Services (AWS AppConfig - Feature Flags)",
            "difficulty": "Medium",
            "question": "Which capability of AWS Systems Manager allows engineering teams to deploy application configurations and feature flags safely and gradually to running applications with automatic rollbacks if errors occur?",
            "options": [
                "AWS AppConfig",
                "AWS CodeCommit",
                "AWS CloudFormation Change Sets",
                "AWS OpsWorks Stacks"
            ],
            "answer": 0,
            "explanation": "AWS AppConfig helps you quickly and safely deploy application configurations and feature toggles to applications of any size. It validates configurations before deployment and monitors alarms to roll back changes automatically if issues arise.",
            "citation": "AWS AppConfig User Guide — Feature Flag Deployment"
        }
    ]
    questions.extend(d3)

    # -------------------------------------------------------------
    # DOMAIN 4: BILLING, PRICING & SUPPORT (7 Questions: Q59 - Q65)
    # -------------------------------------------------------------
    d4 = [
        {
            "id": "aws-clf02-s2-059",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (Compute Savings Plans)",
            "difficulty": "Medium",
            "question": "Which flexible pricing model offers savings of up to 66% in exchange for a commitment to a consistent amount of compute usage (measured in $/hour) for a 1- or 3-year term, applying automatically across EC2, Lambda, and Fargate?",
            "options": [
                "Compute Savings Plans",
                "EC2 Instance Savings Plans",
                "Standard Reserved Instances",
                "Spot Instance Fleet Contracts"
            ],
            "answer": 0,
            "explanation": "Compute Savings Plans provide the greatest flexibility, automatically applying discounts of up to 66% regardless of instance family, size, OS, tenancy, or AWS Region, and applying seamlessly across Amazon EC2, AWS Fargate, and AWS Lambda.",
            "citation": "AWS Cost Management Guide — Understanding Savings Plans"
        },
        {
            "id": "aws-clf02-s2-060",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Free Tier Categories)",
            "difficulty": "Easy",
            "question": "What are the three distinct types of free offers provided by the AWS Free Tier?",
            "options": [
                "Always Free, 12 Months Free, and Short-term Free Trials",
                "Weekly Promos, Monthly Allowances, and Annual Rebates",
                "Executive Trials, Startup Vouchers, and Enterprise Grants",
                "Academic Credits, Beta Access, and Colocation Discounts"
            ],
            "answer": 0,
            "explanation": "The AWS Free Tier offers three distinct categories of free offers: 'Always Free' (e.g., 1 million Lambda requests/mo), '12 Months Free' (available for the first year following initial sign-up, e.g., 750 hrs/mo of t2/t3.micro EC2), and 'Short-term Free Trials.'",
            "citation": "AWS Free Tier Documentation — Categories of Free Services"
        },
        {
            "id": "aws-clf02-s2-061",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (Cost Allocation Tags)",
            "difficulty": "Easy",
            "question": "What mechanism should an organization implement on their AWS resources to organize, categorize, and track cloud costs by department, project name, or cost center in billing reports?",
            "options": [
                "Cost Allocation Tags (Key-Value pairs)",
                "Static IP Address Grouping",
                "Service Control Policies (SCPs)",
                "VPC Subnet Renaming Conventions"
            ],
            "answer": 0,
            "explanation": "Cost Allocation Tags are key-value labels assigned to AWS resources (e.g., CostCenter=Marketing, Project=MobileApp). Once activated in the Billing console, AWS organizes cost reports by these tags for clear financial attribution.",
            "citation": "AWS Billing User Guide — Using Cost Allocation Tags"
        },
        {
            "id": "aws-clf02-s2-062",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Support Plans: Developer Plan)",
            "difficulty": "Easy",
            "question": "Which AWS Support Plan is recommended for early-stage development and testing workloads, offering business-hours email access to Cloud Support Associates for one primary contact with response times under 12 hours?",
            "options": [
                "AWS Developer Support",
                "AWS Basic Support",
                "AWS Business Support",
                "AWS Enterprise Support"
            ],
            "answer": 0,
            "explanation": "The AWS Developer Support plan is designed for non-production environments and early experimentation. It provides business-hours email access to Cloud Support Associates, 1 primary contact, and response times under 12 hours for general guidance.",
            "citation": "AWS Support Plans Guide — Developer Support Tier"
        },
        {
            "id": "aws-clf02-s2-063",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Marketplace)",
            "difficulty": "Easy",
            "question": "Which digital catalog allows customers to find, test, buy, and instantly deploy third-party software applications, AMIs, containers, and SaaS solutions with charges integrated directly into their monthly AWS bill?",
            "options": [
                "AWS Marketplace",
                "AWS Service Catalog",
                "AWS Systems Manager Store",
                "Amazon AppFlow"
            ],
            "answer": 0,
            "explanation": "AWS Marketplace is a curated digital catalog that makes it easy for customers to find, buy, deploy, and manage third-party software, data, and services. Purchases appear seamlessly on the consolidated AWS monthly bill.",
            "citation": "AWS Marketplace Buyer Guide — Overview"
        },
        {
            "id": "aws-clf02-s2-064",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Compute Optimizer)",
            "difficulty": "Medium",
            "question": "Which machine learning-powered service analyzes historical CloudWatch utilization metrics to recommend optimal rightsizing for Amazon EC2 instances, EBS volumes, and Lambda functions to reduce costs and improve performance?",
            "options": [
                "AWS Compute Optimizer",
                "AWS Trusted Advisor",
                "AWS Cost Explorer",
                "AWS Well-Architected Tool"
            ],
            "answer": 0,
            "explanation": "AWS Compute Optimizer uses machine learning to analyze historical resource utilization metrics from CloudWatch and delivers actionable recommendations to rightsize EC2 instances, EBS volumes, and Lambda functions to cut unnecessary costs.",
            "citation": "AWS Compute Optimizer User Guide — Rightsizing Recommendations"
        },
        {
            "id": "aws-clf02-s2-065",
            "type": "mcq",
            "subtopic": "Domain 4: Billing & Support (AWS Health Dashboard)",
            "difficulty": "Easy",
            "question": "Which dashboard provides personalized alerts and proactive notifications about AWS service disruptions, planned maintenance events, and changes that specifically affect the resources in YOUR AWS account?",
            "options": [
                "AWS Health Dashboard (Personal Health Dashboard)",
                "Amazon CloudWatch Service Dashboard",
                "AWS Trusted Advisor Dashboard",
                "AWS CloudTrail Management Event Log"
            ],
            "answer": 0,
            "explanation": "The AWS Health Dashboard provides personalized information about the availability and operations of AWS services and resources in your specific account. It alerts you to active service disruptions and scheduled maintenance windows.",
            "citation": "AWS Health User Guide — Personalized Health Dashboard"
        }
    ]
    questions.extend(d4)

    return questions

def generate_html_runner(set_num, set_name, other_set_num, other_set_name):
    num_str = f"{set_num:02d}"
    other_num_str = f"{other_set_num:02d}"
    
    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AWS Certified Cloud Practitioner Practice Exam {num_str} (CLF-C02) | MockTestVault</title>
  <meta name="description" content="Free 65-question timed AWS Certified Cloud Practitioner (CLF-C02) practice test with 90-min timer, 700/1000 passing score, official domain weightages, and detailed rationales.">
  <!-- Canonical & Open Graph (Social Sharing) -->
  <link rel="canonical" href="https://mocktestvault.com/global/aws/cloud-practitioner-clf-c02-practice-{num_str}.html">
  <meta property="og:site_name" content="MockTestVault">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://mocktestvault.com/global/aws/cloud-practitioner-clf-c02-practice-{num_str}.html">
  <meta property="og:title" content="AWS Certified Cloud Practitioner Practice Exam {num_str} (CLF-C02) | MockTestVault">
  <meta property="og:description" content="Free 65-question timed AWS Certified Cloud Practitioner (CLF-C02) practice test with 90-min timer, 700/1000 passing score, official domain weightages, and detailed rationales.">
  <meta property="og:image" content="https://mocktestvault.com/assets/og-image.png">
  <meta property="og:image:secure_url" content="https://mocktestvault.com/assets/og-image.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="MockTestVault — Free Online CBT Mock Exam Simulator">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="AWS Certified Cloud Practitioner Practice Exam {num_str} (CLF-C02) | MockTestVault">
  <meta name="twitter:description" content="Free 65-question timed AWS Certified Cloud Practitioner (CLF-C02) practice test with 90-min timer, 700/1000 passing score, official domain weightages, and detailed rationales.">
  <meta name="twitter:image" content="https://mocktestvault.com/assets/og-image.png">
  <meta name="twitter:image:alt" content="MockTestVault — Free Online CBT Mock Exam Simulator">

  <link rel="stylesheet" href="../../css/test-engine.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "AWS Certified Cloud Practitioner (CLF-C02) Practice Exam {num_str}",
    "description": "Full-length 65-question timed practice exam adhering strictly to the official AWS CLF-C02 certification domains: Cloud Concepts (24%), Security & Compliance (30%), Cloud Technology & Services (34%), and Billing & Pricing (12%).",
    "educationalLevel": "Professional Certification • Cloud Computing (Amazon Web Services)",
    "learningResourceType": "Full Practice Exam",
    "provider": {{
      "@type": "Organization",
      "name": "MockTestVault",
      "url": "https://mocktestvault.com"
    }}
  }}
  </script>
  <link rel="manifest" href="/manifest.json">
  <meta name="theme-color" content="#2563eb">

  <!-- Schema.org BreadcrumbList Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://mocktestvault.com/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Global Exam Vault",
        "item": "https://mocktestvault.com/global/"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "AWS Cloud Practitioner Practice {num_str}",
        "item": "https://mocktestvault.com/global/aws/cloud-practitioner-clf-c02-practice-{num_str}.html"
      }}
    ]
  }}
  </script>
</head>
<body>

  <!-- Print Only Header -->
  <div class="print-only-header">
    <div class="print-title" role="heading" aria-level="2">MockTestVault Global — AWS Certified Cloud Practitioner Practice Exam {num_str}</div>
    <p>Official Amazon Web Services CLF-C02 Certification Standard | 65 Questions • 90 Minutes | mocktestvault.com</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">☁️</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">AWS CLF-C02</span></h1>
          <p>Certified Cloud Practitioner Simulator</p>
        </div>
      </a>

      <div class="header-controls">
        <div class="mode-pill-group" role="group" aria-label="Test Mode Selection">
          <button id="mode-practice-btn" class="mode-btn" title="Practice Mode: Instant answers and official AWS documentation citations">
            <span>🎓</span> Practice
          </button>
          <button id="mode-exam-btn" class="mode-btn active" title="Exam Mode: Timed 90-min official certification simulation with 700/1000 scale">
            <span>⏱️</span> Exam
          </button>
        </div>

        <div style="display:flex; gap:6px;">
          <button id="btn-font-dec" class="tool-btn" title="Decrease Font Size">A-</button>
          <button id="btn-font-inc" class="tool-btn" title="Increase Font Size">A+</button>
          <button id="btn-sound-toggle" class="tool-btn" title="Toggle Sound Feedback">🔊</button>
          <button id="btn-fullscreen-toggle" class="tool-btn" title="Toggle Fullscreen Focus">⛶</button>
        </div>

        <button id="theme-toggle-btn" class="theme-toggle-btn" title="Toggle Dark/Light Mode">🌙</button>
      </div>
    </div>
  </header>

  <!-- Breadcrumb Navigation -->
  <nav class="breadcrumb-bar" aria-label="Breadcrumb">
    <div class="breadcrumb-container">
      <a href="../../index.html">Home</a>
      <span class="sep">/</span>
      <a href="../index.html">Global Exam Vault</a>
      <span class="sep">/</span>
      <span class="current">AWS Cloud Practitioner Practice {num_str} (65 Qs)</span>
    </div>
  </nav>

  <!-- Multi-Set Selector Bar (130 Total Questions) -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">CLF-C02 Full Practice Exams:</span>
      <div class="set-btn-group" role="tablist">
        <a href="cloud-practitioner-clf-c02-practice-01.html" class="set-btn {'active' if set_num == 1 else ''}" role="tab" aria-selected="{'true' if set_num == 1 else 'false'}">
          <span>☁️ Full Practice Exam 01</span>
          <span class="set-badge-count">65 Qs • 90M</span>
        </a>
        <a href="cloud-practitioner-clf-c02-practice-02.html" class="set-btn {'active' if set_num == 2 else ''}" role="tab" aria-selected="{'true' if set_num == 2 else 'false'}">
          <span>☁️ Full Practice Exam 02</span>
          <span class="set-badge-count">65 Qs • 90M</span>
        </a>
      </div>
    </div>
  </div>

  <!-- Exam Live Status Bar -->
  <div id="exam-status-bar" class="exam-status-bar">
    <div class="status-container">
      <div id="timer-box" class="timer-box">
        <span>⏱️</span>
        <span id="timer-display">90:00</span>
      </div>

      <div class="progress-info">
        <span id="progress-text" class="progress-text">0 of 65 answered (0%)</span>
        <div class="progress-bar-track">
          <div id="progress-bar-fill" class="progress-bar-fill"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Split Layout -->
  <main class="test-layout" id="test-layout">
    
    <!-- Question Card -->
    <section class="question-card" id="question-card" aria-label="Active Test Question">
      <div class="meta-badges-row" id="q-badges"></div>

      <div class="question-scroll-body">
        <div class="question-text-box">
          <div class="question-number" id="q-number">Question 1 of 65</div>
          <div class="question-title" id="q-title">Loading questions...</div>
        </div>

        <div class="options-list" id="options-list" role="radiogroup" aria-label="Answer choices"></div>

        <div class="explanation-box" id="explanation-box">
          <div class="explanation-title" id="exp-status"></div>
          <div class="explanation-text" id="explanation-text"></div>
          <div class="citation-tag" id="citation-tag"></div>
        </div>
      </div>

      <!-- Persistent Action Bar (Pinned to Card Bottom) -->
      <div class="card-action-bar">
        <div class="action-buttons-group">
          <button id="btn-prev" class="nav-btn" disabled>
            <span>← Previous</span>
          </button>
          
          <button id="btn-review" class="nav-btn btn-review">
            <span>🚩 Mark for Review</span>
          </button>
          
          <button id="btn-clear" class="nav-btn">
            <span>🧹 Clear</span>
          </button>
          
          <button id="btn-next" class="nav-btn btn-primary">
            <span>Next →</span>
          </button>

          <button id="btn-open-submit" class="nav-btn btn-submit-test">
            <span>Submit Test 🏁</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Side Question Palette -->
    <aside class="palette-card" aria-label="Question Navigation Palette">
      <div class="palette-title">
        <span>Question Palette</span>
        <span class="palette-count-badge">65 Questions</span>
      </div>

      <div class="palette-grid" id="palette-grid" role="navigation" aria-label="Question Jump Grid"></div>

      <div class="palette-legend">
        <div class="legend-item">
          <span class="legend-dot dot-answered"></span>
          <span>Answered (<span id="count-answered">0</span>)</span>
        </div>
        <div class="legend-item">
          <span class="legend-dot dot-not-answered"></span>
          <span>Not Answered (<span id="count-not-answered">0</span>)</span>
        </div>
        <div class="legend-item">
          <span class="legend-dot dot-reviewed"></span>
          <span>Marked for Review (<span id="count-reviewed">0</span>)</span>
        </div>
        <div class="legend-item">
          <span class="legend-dot dot-answered-reviewed"></span>
          <span>Ans &amp; Marked for Review (<span id="count-ans-reviewed">0</span>)</span>
        </div>
        <div class="legend-item">
          <span class="legend-dot dot-unvisited"></span>
          <span>Not Visited (<span id="count-unvisited">65</span>)</span>
        </div>
      </div>
    </aside>

  </main>

  <!-- Scorecard Result Modal -->
  <section class="scorecard-view" id="scorecard-view" style="display:none;" aria-label="Exam Results and Scorecard">
    <div class="score-hero" id="score-hero"></div>
    <div class="stats-grid" id="stats-grid"></div>
    <div class="mastery-container" id="mastery-container"></div>

    <div class="review-actions-bar">
      <div class="filter-btn-group" role="group" aria-label="Review Filter Options">
        <button id="filter-all" class="filter-btn active">All Questions</button>
        <button id="filter-wrong" class="filter-btn">Incorrect Only</button>
        <button id="filter-reviewed" class="filter-btn">Flagged for Review</button>
      </div>

      <div style="display:flex; gap:10px;">
        <button id="btn-retake" class="nav-btn btn-primary">Retake Exam</button>
        <button id="btn-print" class="nav-btn">Print Scorecard</button>
      </div>
    </div>

    <div id="review-list"></div>
  </section>

  <!-- Static Educational Overview & Candidate Instructions -->
  <section class="exam-guide-static" style="max-width:1100px; margin:36px auto 48px auto; padding:28px 24px; background:var(--bg-surface); border:1px solid var(--border-color); border-radius:var(--radius-lg); box-shadow:var(--shadow-sm);">
    <noscript>
      <div style="padding:16px 20px; background:#fff3cd; color:#856404; border:1px solid #ffeeba; border-radius:8px; margin-bottom:24px; font-size:0.92rem; line-height:1.5;">
        <strong>⚠️ JavaScript Recommended:</strong> This AWS CLF-C02 simulator requires JavaScript for the 90-minute countdown, domain scoring, and instant answer rationales.
      </div>
    </noscript>

    <div style="border-bottom:2px solid var(--primary-light); padding-bottom:12px; margin-bottom:20px;">
      <h2 style="font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:6px;">
        ☁️ AWS Certified Cloud Practitioner (CLF-C02) Blueprint
      </h2>
      <p style="font-size:0.88rem; color:var(--text-muted); margin:0;">
        Official Amazon Web Services Exam Guide: 65 Questions • 90 Minutes • Passing Benchmark: 700 / 1000 Scaled Points
      </p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:16px; margin-bottom:20px;">
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); display:block; margin-bottom:4px; font-size:0.92rem;">1. Cloud Concepts (24% ~ 16 Qs)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">Cloud value proposition, CapEx vs OpEx, economies of scale, and the 6 Well-Architected Framework pillars.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); display:block; margin-bottom:4px; font-size:0.92rem;">2. Security &amp; Compliance (30% ~ 20 Qs)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">Shared Responsibility Model, IAM roles &amp; MFA, Security Groups vs NACLs, AWS WAF, Shield, KMS, and Artifact.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); display:block; margin-bottom:4px; font-size:0.92rem;">3. Cloud Technology &amp; Services (34% ~ 22 Qs)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">Compute (EC2, Lambda, Fargate), Storage (S3, EBS, EFS), Databases (RDS, Aurora, DynamoDB), and VPC networking.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); display:block; margin-bottom:4px; font-size:0.92rem;">4. Billing, Pricing &amp; Support (12% ~ 7 Qs)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">Cost Explorer, AWS Budgets, Pricing Calculator, Consolidated Billing, and the 4 AWS Support plans.</span>
      </div>
    </div>

    <div style="background:var(--bg-subtle); border-radius:8px; padding:18px; margin-bottom:24px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">⚖️ Official Scoring &amp; Passing Threshold:</strong>
      • <strong>Passing Score:</strong> 700 out of 1000 scaled points (~70% raw threshold).<br>
      • <strong>Zero Negative Marking:</strong> There is no penalty for guessing. Unanswered items receive zero points. Always select an answer for every question.<br>
      • <strong>Exam Strategy:</strong> Flag unfamiliar scenarios and complete rapid-fire recall questions first (Cloud Concepts and Billing) before tackling multi-clause architectural networking questions.
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <p><strong>MockTestVault.com</strong> — 100% Free Educational Practice &amp; Professional Certification Simulators.</p>
      <p style="font-size:0.75rem;">Aligned with official Amazon Web Services (AWS) CLF-C02 examination standards. AWS® is a registered trademark of Amazon.com, Inc. or its affiliates, which is not affiliated with this website.</p>
    
    <div class="footer-legal-links">
      <a href="/about.html">About Us</a>
      <span class="sep">•</span>
      <a href="/privacy.html">Privacy Policy</a>
      <span class="sep">•</span>
      <a href="/terms.html">Terms of Service</a>
      <span class="sep">•</span>
      <a href="/disclaimer.html">Academic Disclaimer</a>
      <span class="sep">•</span>
      <a href="/contact.html">Contact &amp; Support</a>
      <span class="sep">•</span>
      <a href="/progress.html">Curriculum Tracker</a>
    </div>
    </div>
  </footer>

  <script src="../../js/test-engine.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      window.testEngine = new MockTestEngine({{
        initialSet: 'set{set_num}',
        timeLimitMinutes: 90,
        randomSampleSize: 65,
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'competitive',
        setSources: {{
          set1: '../../data/global/aws/aws_clf_c02_practice_set1.json',
          set2: '../../data/global/aws/aws_clf_c02_practice_set2.json'
        }}
      }});
      window.testEngine.loadQuestions();
    }});
  </script>
</body>
</html>
"""
    return html

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data", "global", "aws")
    runner_dir = os.path.join(base_dir, "global", "aws")
    
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(runner_dir, exist_ok=True)
    
    q1 = get_questions_set1()
    q2 = get_questions_set2()
    
    print(f"Set 1 Questions: {len(q1)}")
    print(f"Set 2 Questions: {len(q2)}")
    assert len(q1) == 65, f"Set 1 must have exactly 65 questions, got {len(q1)}"
    assert len(q2) == 65, f"Set 2 must have exactly 65 questions, got {len(q2)}"
    
    # Save JSON files
    set1_json_path = os.path.join(data_dir, "aws_clf_c02_practice_set1.json")
    with open(set1_json_path, "w", encoding="utf-8") as f:
        json.dump({"questions": q1}, f, indent=2)
    print(f"Saved: {set1_json_path}")

    set2_json_path = os.path.join(data_dir, "aws_clf_c02_practice_set2.json")
    with open(set2_json_path, "w", encoding="utf-8") as f:
        json.dump({"questions": q2}, f, indent=2)
    print(f"Saved: {set2_json_path}")
    
    # Save HTML runners
    runner1_path = os.path.join(runner_dir, "cloud-practitioner-clf-c02-practice-01.html")
    with open(runner1_path, "w", encoding="utf-8") as f:
        f.write(generate_html_runner(1, "Full Practice Exam 01", 2, "Full Practice Exam 02"))
    print(f"Saved: {runner1_path}")

    runner2_path = os.path.join(runner_dir, "cloud-practitioner-clf-c02-practice-02.html")
    with open(runner2_path, "w", encoding="utf-8") as f:
        f.write(generate_html_runner(2, "Full Practice Exam 02", 1, "Full Practice Exam 01"))
    print(f"Saved: {runner2_path}")

if __name__ == "__main__":
    main()
