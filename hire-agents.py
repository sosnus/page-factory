import os

# Define the folder and file structure
agents_dir = "agents"
agents_files = {
    "theme-agent.txt": """You are a Hugo theme developer.
Your task is to generate Hugo templates, partials, CSS, JS, and layouts.
Follow Hugo best practices, use modern CSS, and maintain a clear folder structure.
Provide the file path and content for each file.
""",
    "content-agent.txt": """You are a Hugo content writer.
Generate blog posts, pages, or Markdown content with front matter.
Use Hugo shortcodes where relevant.
Keep content clear, engaging, and formatted properly for Hugo.
"""
}

# Create the agents directory if it doesn't exist
os.makedirs(agents_dir, exist_ok=True)

# Create and write the agent files
for filename, content in agents_files.items():
    file_path = os.path.join(agents_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Created {file_path}")

print("\nAll agent prompt files created successfully!")