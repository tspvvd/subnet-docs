# subnet-docs

This repository serves as a centralized knowledge base for all subnet information within the Bittensor ecosystem. It provides structured documentation for each subnet to help users, developers, and stakeholders understand their purpose, technical specifications, and operational details. This is also currently in use by [Backprop Finance](https://backprop.finance/) by Tensorplex Labs.

## How to Add Your Subnet Information

Thank you for your interest in adding your subnet to our documentation! Follow these steps to ensure your subnet information is properly included:

### 1. Folder Structure

Create a new folder in the repository under the `data` directory using your subnet's netuid as the folder name:

```
subnet-docs/
├── data/
│   ├── 1/                  # Subnet netuid
│   │   ├── subnet.json     # Required
│   │   └── description.html  # Optional
│   ├── <YOUR_NETUID>/      # Your subnet's netuid
│   │   ├── subnet.json     # Required
│   │   └── description.html  # Optional
```

### 2. Required Documentation

#### subnet.json (Mandatory)

Your subnet folder must contain a `subnet.json` file that follows the schema format. Here's an example template based on SN1:

```json
{
  "$schema": "../../schema.json",
  "bittensor_id": "your_identifier",
  "letter": "𝛼",                     // Greek or other letter representing your subnet
  "name": "Your Subnet Name",
  "github": ["https://github.com/your-org/your-repo"],
  "hw_requirements": "https://github.com/your-org/your-repo/hardware-specs.md",
  "image_url": "https://example.com/your-subnet-logo.png", // For more details, please refer to the following section about how to upload token images
  "description": "description.html",  // Reference to optional HTML file. If description.html is not provided, please leave this field empty.
  "bittensor_discord_id": "discord_channel_id",
  "team": "Your Team Name",
  "summary": "Brief summary of your subnet's purpose and functionality.",
  "categories": ["Category1", "Category2"], // Defined in categories.json. Please refer to the following section about how to add a new category.
  "websites": [
    {
      "label": "twitter", // ALl supported labels: website, dashboard, telegram, discord, github, reddit, youtube, linkedin, medium, whitepaper.
      "url": "https://x.com/YourHandle"
    },
    {
      "label": "website",
      "url": "https://www.yourwebsite.com"
    },
    {
      "label": "dashboard",
      "url": "https://www.yourwebsite.com/dashboard"
    }
  ]
}
```

### 3. Images and Additional Resources

- We will host your subnet logo at a stable URL (referenced in the `image_url` field), therefore please provide a downloable link for the image in the PR and we will host it for you. The image should have a minimum resolution of 128x128. The following formats are supported: SVG, PNG, JPG, WEBP.
- description.html is optional. You may provide a more detailed description with HTML formatting in a `description.html` file. If not provided, please leave this field empty.
- To add a new category that is not already defined in `categories.json`, please include justification in the PR.

## Contribution Process

1. Fork this repository
2. Create a new branch for your subnet documentation
3. Add your subnet folder with the required `subnet.json` and optional `description.html` files
4. Submit a pull request with a clear description of your subnet
5. Once approved, your subnet documentation will be merged and published


## Additonal Info: How the Documentation is Generated

The `generate_subnets.py` script processes all subnet folders and generates consolidated documentation:

- It scans all directories in the `data/` folder
- Processes each subnet's `subnet.json` file and incorporates the `description.html` content when available
- Validates the JSON against the schema to ensure all required fields are present
- Generates standardized output files with consistent formatting for downstream use (e.g. Subnet Info page on Backprop Finance)

> **Note**: The script automatically runs when changes are merged to the main branch, so you don't need to run it manually.



## Questions or Issues?

If you have any questions about adding your subnet documentation, please open an issue in this repository or reach out to us.

Thank you for contributing to our subnet documentation!
