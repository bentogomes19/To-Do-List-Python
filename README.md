# To-do List - Python + SQLite3 

### Sobre o sistema
- O To-do list é uma ferramenta de gerenciamento de tarefas para facilitar as pessoas a gerenciar suas tarefas no cotidiano. 

***Ferramentas utilizadas***
- Python 3.12.0
- Banco de Dados: SQLite3
- Terminal
- VM VirtualBox para testes (Windows)

***Ambiente de Desenvovimento***
- IDE: Pycharm Community 2024
- GNU/Linux Manjaro

### Requsitos Funcionais
- ***RF01***: O sistema deve permitir ao usuário criar uma tarefa
- ***RF02***: O sistema deve permitir ao usuário editar uma tarefa
- ***RF03***: O sistema deve permitir ao usuário excluir uma tarefa
- ***RF04***: O sistema deve permitir ao usuário marcar uma tarefa como concluída
- ***RF05***: O sistema deve exibir todas as tarefas pendentes e concluídas, separando-as adequadamente
- ***RF06***: O sistema deve permitir que o usuário filtre as tarefas por estado (pendente//concluída)
- ***RF07***: O sistema deve salvar as tarefas em um banco de dados, e ao reiniciar, deve carregar a lista de tarefas previamente salva.
- ***RF08***: O sistema deve permitir a busca por tarefas específicas usando palavras-chaves

#### Requisitos Não Funcionais
- ***RNF01***: ***Performance***:  o tempo de resposta para adicionar, remover ou exibir uma tarefa deve ser inferior a 1 seg.
- **RNF02**: ***Compatibilidade***: O sistema deve ser compatível com diferentes sistemas operacionais, incluindo Linux, MacOS e Windows, desde que o terminal suporte Python e SQLite
- **RNF03**: ***Usabilidade***: O sistema deve ter uma interface de linha de comando simples, com instruções claras para o usuário. A sintaxe dos comandos deve ser intuitiva e fácil de usar.
- **RNF04**: ***Portablidade***: O código deve ser portátil, permitindo fácil adaptação a outros ambientes de terminal sem necessidade de grandes mudanças.
- **RNF05**: ***Persistência de Dados***: O sistema deve salvar os dados de forma persistente, em um banco de dados para que as informações não sejam perdidas quando o programa for encerrado.
- **RNF06**: ***Segurança***: O sistema deve garantir que os dados salvos sejam consistentes e protegidos contra corrupção, mesmo que haja falhas inesperadas ou encerramentos abruptos.

### Modelo de Entidade e Relacionamento (DER)

### Tabela do Banco de Dados 

### Funcionalidade do sistema
- O programa funciona em um shell de sua preferência, não há um uso de uma interface gráfica. OBS: Em projetos futuros de ampliação o sistema irá conter uma interface gráfica de usuário.





