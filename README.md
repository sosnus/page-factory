# page-factory

## install
```bash
sudo snap install hugo #should install version 0.160
```

## active hugo
```bash
hugo new site page-framework
```

## Add info to config.toml
```toml
[module]
  [[module.imports]]
    disable = false
    ignoreConfig = false
    ignoreImports = false
    path = 'github.com/theNewDynamic/gohugo-theme-ananke/v2'
```

## active go mod
```bash
go mod init github.com/sosnus/page-factory/page-framework
```

## active go mod
```bash
hugo server -M
```




## AI Commands
```bash
ollama run mistral
```

## OLD wake up agents
```bash
ollama create agent theme-agent --model mistral-7b --prompt-file agents/theme-agent.txt
ollama create agent content-agent --model mistral-7b --prompt-file agents/content-agent.txt
```

## Models
```bash
ollama run hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:Q4_K_M
```


# hugo

## hugo commands

### build new pages
```bash
# Uses default.md archetype
hugo new content/posts/my-post.md

# Uses archetypes/blog.md if it exists, otherwise default.md
hugo new -k blog content/posts/my-post.md

# Or organize by folder - Hugo auto-applies archetype matching the folder name
hugo new content/blog/my-post.md  # tries archetypes/blog.md first
```