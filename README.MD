# Fluxo do desenvolvimento:
- Primeiro vá para a branch principal `git checkout develop`
- Depois de um `git pull` para que puxe as atualizações
- Crie uma branch nova: `git checkout -b nome_da_branch`
- Depois que fizer as alterações liste os arquivos alterados: `git status`
- Adicione os arquivos desejados com: `git add nome_do_arquivo`, ou então `git add .` caso deseje enviar todos arquivos
- Se tiver algum arquivo que não quer enviar utilize o comando `git restore nome_do_arquivo`, isso reseta o arquivo em que mexeu
- Comite as alterações `git commit -m mensagem_do_commit`
- Depois disso dê o comando `git pull --rebase origin develop` para puxar qualquer outra atualização que tenha tido na branch develop
- Agora pode enviar as alterações para a branch `git push origin branch_em_que_está`
- Ai lá no gitlab, crie um merge request dessa branch pra develop.
- Depois disso eu vou xingar o código que vc enviou e juntar na develop





Tutorial de login pra ver depois: https://learndjango.com/tutorials/django-login-and-logout-tutorial