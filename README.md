# Domain-Specific PDF Summarization & Keyword Extraction Pipeline
## Project Overview
This project implements a dynamic, high-performance pipeline that ingests, processes, and stores summaries and keywords for multiple PDF documents. Designed to handle a range of PDF sizes (short to long), this pipeline extracts relevant summaries and domain-specific keywords, storing them in a MongoDB collection. The project emphasizes concurrency, innovation, and custom implementations over pre-built frameworks to maximize efficiency.

## Features
PDF Ingestion & Parsing: Efficiently ingests PDF files of varying lengths from a specified folder.
Concurrency: Processes multiple PDFs concurrently to optimize speed and performance.
Summarization & Keyword Extraction: Dynamically generates summaries and extracts non-generic, domain-specific keywords based on document content.
Database Storage: Stores metadata, summaries, and keywords for each PDF in MongoDB, ensuring structured JSON updates.
Error Handling: Logs and manages errors for corrupted PDFs or unsupported formats without affecting the overall workflow.
Performance Monitoring: Tracks concurrency, memory usage, and processing speed.
## Project Structure
pdf_pipeline/
│
├── main.py              # Entry point for the pipeline execution
├── pipeline.py          # Core pipeline logic handling ingestion and processing
├── summarization.py     # Custom summarization module
├── keywords.py          # Keyword extraction module
├── mongodb.py           # MongoDB connection and data insertion
├── utils.py             # Utility functions for parsing PDFs
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation

## Requirements
The required packages are listed in requirements.txt. 

## Key Modules
pipeline.py: Manages PDF ingestion, processing, and data flow.
summarization.py: Contains the summarization logic.
keywords.py: Implements custom keyword extraction.
mongodb.py: Handles MongoDB connections and data storage.

## Performance & Testing
Concurrency: Designed to handle concurrent processing of multiple PDFs.
Performance Metrics: Monitors and logs processing time for each PDF.
Error Handling: Logs errors for problematic PDFs, including corrupted or encrypted files, to ensure they don’t impact the entire pipeline.
Innovation & Customization
This pipeline avoids pre-built frameworks wherever possible to deliver a streamlined, high-performance, custom solution tailored to PDF summarization and keyword extraction.

## Future Improvements
Dockerization: Deploy the project in a Docker container for simplified setup and portability.
Web Interface: Add a simple web interface for easier user interaction.
Advanced NLP: Implement advanced NLP techniques for improved keyword extraction and summarization accuracy.
