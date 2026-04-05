# page-factory

## install
```bash
sudo snap install hugo #should install version 0.160
```

## active hugo
```bash
hugo new site page-framework
```

## wake up agents
```bash
ollama create agent theme-agent --model mistral-7b --prompt-file agents/theme-agent.txt
ollama create agent content-agent --model mistral-7b --prompt-file agents/content-agent.txt
```

