# Perguntas
## 1) Você acha que este código está estruturado, legível e escalável?
<p>Não, o código consta com apenas uma simples página, por mais que esteja legível, sua escalabilidade ao ser incluído novos requisitos, a complexidade vai aumentando e tornando a manutenção mais difícil futuramente.</p>

## 2) O que você mudaria nos arquivos e na estrutura de pastas para melhorá-lo nesse sentido?
<p>Estruturar em múltiplos arquivos bem definidos, com baixo acoplamento, tornando a manutenção futura e tornando possível manipulação por múltiplos programadores.</p>

## 3) Quanto a arquitetura API e sua conteinerização, liste as brechas de segurança que você identificou neste código? Como você as resolveria?

<p>Caso haja a exposição do código fonte, o fato de os dados referentes ao db estar no repositório, torna possível a exposição publicamente, ou por acesso não autorizado, outro ponto a destacar é o acesso da api de modo externo, um fator de authenticação jwt resolveria tal problema.</p>