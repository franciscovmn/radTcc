CURSOS = [
    ("Tecnologia em Sistemas para Internet", "TSI"),
    ("Licenciatura em Matemática", "LMAT"),
    ("Engenharia Elétrica", "ELE"),
    ("Administração", "ADM"),
]

ORIENTADORES = [
    ("Renata Albuquerque Lima", "Doutora", "renata.lima@ifpb.edu.br"),
    ("Carlos Eduardo Pontes", "Mestre", "carlos.pontes@ifpb.edu.br"),
    ("Mariana Cavalcanti Rocha", "Doutora", "mariana.rocha@ifpb.edu.br"),
    ("José Antônio Barbosa", "Doutor", "jose.barbosa@ifpb.edu.br"),
    ("Patrícia Nunes Moura", "Doutora", "patricia.moura@ifpb.edu.br"),
    ("Fernando Sales Medeiros", "Mestre", "fernando.medeiros@ifpb.edu.br"),
    ("Luciana Ferreira Duarte", "Doutora", "luciana.duarte@ifpb.edu.br"),
    ("Ricardo Tavares Souto", "Especialista", "ricardo.souto@ifpb.edu.br"),
]

# orientadores (índices de ORIENTADORES) disponíveis em cada curso
ORIENTADORES_POR_CURSO = {
    "TSI": [0, 1, 2, 3],
    "LMAT": [4, 5],
    "ELE": [6, 2],
    "ADM": [7, 5],
}

PALAVRAS_CHAVE = [
    "aprendizagem de máquina",
    "desenvolvimento web",
    "acessibilidade",
    "banco de dados",
    "segurança da informação",
    "internet das coisas",
    "educação a distância",
    "energia solar",
    "automação",
    "gestão de projetos",
    "ensino de matemática",
    "dispositivos móveis",
    "sustentabilidade",
    "análise de dados",
    "redes de computadores",
]

NOMES = [
    "Ana Beatriz", "Lucas", "Camila", "Gabriel", "Juliana", "Rafael", "Larissa",
    "Mateus", "Beatriz", "Pedro", "Isabela", "Thiago", "Letícia", "Bruno",
    "Natália", "Diego", "Amanda", "Felipe", "Carolina", "Vinícius", "Raquel",
    "Gustavo", "Priscila", "Leonardo", "Débora", "Henrique", "Tatiane", "Samuel",
    "Vanessa", "Igor", "Aline", "Rodrigo", "Jéssica", "Caio",
]

SOBRENOMES = [
    "Silva Santos", "Oliveira Costa", "Pereira Lima", "Almeida Souza",
    "Ribeiro Alves", "Carvalho Dias", "Gomes Ferreira", "Martins Araújo",
    "Barros Nogueira", "Cunha Teixeira", "Freitas Monteiro", "Pinto Campos",
    "Lopes Batista", "Ramos Vieira", "Machado Rezende", "Correia Brito",
    "Andrade Melo", "Moreira Xavier", "Cardoso Farias", "Azevedo Peixoto",
    "Rocha Bezerra", "Siqueira Leite", "Fonseca Queiroz", "Nascimento Paiva",
    "Guedes Sampaio", "Valente Torres", "Borges Lacerda", "Furtado Mendes",
    "Coelho Viana", "Marques Padilha", "Toledo Arruda", "Salgado Pessoa",
    "Matos Figueiredo", "Brandão Esteves",
]

# (título, curso, ano, situação, palavras-chave, nº de autores, resumo)
TRABALHOS = [
    (
        "Sistema web para gestão de monitorias em cursos técnicos",
        "TSI", 2021, "publicado", [1, 3], 1,
        "Desenvolvimento de uma aplicação web para cadastro de monitores, controle de horários e registro de atendimentos. O sistema substituiu planilhas compartilhadas usadas pela coordenação.",
    ),
    (
        "Detecção de plágio em trabalhos acadêmicos com aprendizado de máquina",
        "TSI", 2022, "publicado", [0, 13], 1,
        "Avaliação de modelos de similaridade textual para identificar trechos copiados em monografias. Os resultados comparam precisão e tempo de processamento em um corpus de trabalhos defendidos.",
    ),
    (
        "Aplicativo móvel para acompanhamento de hábitos de estudo",
        "TSI", 2022, "publicado", [11, 1], 1,
        "Aplicativo que registra sessões de estudo e gera relatórios semanais para o estudante. A validação foi feita com uma turma do curso técnico integrado.",
    ),
    (
        "Análise de vulnerabilidades em aplicações web de instituições públicas",
        "TSI", 2023, "publicado", [4, 1], 2,
        "Levantamento de falhas comuns, como injeção de SQL e controle de acesso inadequado, em portais públicos. O trabalho propõe um checklist de verificação baseado na lista OWASP.",
    ),
    (
        "Monitoramento de consumo de água com dispositivos IoT de baixo custo",
        "TSI", 2023, "publicado", [5, 12], 1,
        "Protótipo com sensores de vazão e microcontroladores que envia leituras para um painel web. Os testes mostraram redução do desperdício em um bloco do campus.",
    ),
    (
        "Painel de indicadores acadêmicos com visualização de dados",
        "TSI", 2024, "publicado", [13, 3], 1,
        "Construção de um painel que consolida taxas de aprovação, evasão e retenção a partir de bases do sistema acadêmico, com filtros por curso e período.",
    ),
    (
        "Acessibilidade em portais de universidades federais",
        "TSI", 2024, "publicado", [2, 1], 1,
        "Auditoria de conformidade com as diretrizes WCAG em portais institucionais, com análise automatizada e revisão manual por leitores de tela.",
    ),
    (
        "Otimização de consultas em bancos de dados relacionais para sistemas acadêmicos",
        "TSI", 2025, "publicado", [3, 13], 1,
        "Estudo do impacto de índices e reescrita de consultas no tempo de resposta de relatórios de notas e frequência em bases com milhões de registros.",
    ),
    (
        "Chatbot para atendimento de dúvidas sobre matrícula",
        "TSI", 2025, "publicado", [0, 6], 1,
        "Implementação de um assistente conversacional treinado com perguntas frequentes da secretaria. A avaliação com estudantes apontou queda no volume de atendimentos presenciais.",
    ),
    (
        "Arquitetura de APIs REST para integração entre sistemas escolares",
        "TSI", 2025, "defendido", [1, 3, 14], 1,
        "Proposta de arquitetura em camadas para expor dados de matrícula e frequência a sistemas externos, com autenticação por token e controle de versões.",
    ),
    (
        "Análise de tráfego em redes sem fio do campus",
        "TSI", 2026, "defendido", [14, 0], 1,
        "Coleta e classificação de tráfego da rede Wi-Fi para identificar horários de pico e aplicações de maior consumo, com apoio de aprendizado de máquina.",
    ),
    (
        "Plataforma de gerenciamento de laboratórios de informática",
        "TSI", 2026, "em_andamento", [1, 9], 1,
        "Sistema para agendamento de laboratórios, controle de equipamentos e abertura de chamados de manutenção.",
    ),
    (
        "Jogos digitais no ensino de funções do primeiro grau",
        "LMAT", 2021, "publicado", [10, 6], 1,
        "Aplicação de jogos digitais em sequências didáticas sobre funções afins. Os resultados comparam o desempenho de duas turmas do primeiro ano do ensino médio.",
    ),
    (
        "Resolução de problemas e o uso de planilhas eletrônicas no ensino médio",
        "LMAT", 2022, "publicado", [10, 13], 1,
        "Investigação do uso de planilhas como ferramenta de modelagem em problemas de proporcionalidade e estatística básica.",
    ),
    (
        "Ensino de geometria com realidade aumentada",
        "LMAT", 2023, "publicado", [10, 11], 2,
        "Uso de aplicativos de realidade aumentada para visualização de sólidos geométricos. A pesquisa discute ganhos na compreensão de volume e planificação.",
    ),
    (
        "Dificuldades de aprendizagem em álgebra na educação de jovens e adultos",
        "LMAT", 2023, "publicado", [10, 6], 1,
        "Estudo de caso sobre erros recorrentes na manipulação de expressões algébricas e estratégias de intervenção em turmas noturnas.",
    ),
    (
        "Modelagem matemática aplicada à sustentabilidade em escolas públicas",
        "LMAT", 2024, "publicado", [10, 12], 1,
        "Projeto de modelagem com dados de consumo de energia e água da própria escola, conduzido por estudantes do ensino fundamental.",
    ),
    (
        "Educação financeira no currículo de matemática",
        "LMAT", 2025, "em_andamento", [10, 9], 1,
        "Análise de propostas para inserir educação financeira em aulas de juros, porcentagem e progressões.",
    ),
    (
        "Dimensionamento de sistema fotovoltaico para prédios públicos",
        "ELE", 2021, "publicado", [7, 12], 1,
        "Estudo de viabilidade técnica e econômica da instalação de painéis fotovoltaicos em um prédio administrativo, com estimativa de retorno do investimento.",
    ),
    (
        "Automação residencial com microcontroladores",
        "ELE", 2022, "publicado", [8, 5], 1,
        "Desenvolvimento de um sistema de controle de iluminação e tomadas com comunicação sem fio e acionamento por aplicativo.",
    ),
    (
        "Eficiência energética em instalações do campus",
        "ELE", 2023, "publicado", [7, 12], 1,
        "Diagnóstico do consumo de energia elétrica em laboratórios e salas de aula, com proposta de substituição de luminárias e ajuste de climatização.",
    ),
    (
        "Controle de irrigação automatizado com sensores de umidade",
        "ELE", 2024, "publicado", [8, 5], 2,
        "Projeto de um controlador que aciona a irrigação conforme a umidade do solo, avaliado em uma horta experimental.",
    ),
    (
        "Qualidade de energia em redes de distribuição urbanas",
        "ELE", 2025, "publicado", [7, 13], 1,
        "Medição de harmônicos e variações de tensão em alimentadores urbanos e análise dos dados segundo as normas da distribuidora.",
    ),
    (
        "Gerenciamento de carga em microrredes com armazenamento",
        "ELE", 2026, "defendido", [7, 8], 1,
        "Simulação de estratégias de despacho de carga em uma microrrede com baterias e geração solar.",
    ),
    (
        "Gestão de projetos em pequenas empresas de tecnologia",
        "ADM", 2021, "publicado", [9], 1,
        "Pesquisa com empresas de software da região sobre adoção de metodologias ágeis e ferramentas de acompanhamento de prazos.",
    ),
    (
        "Impacto da transformação digital no comércio local",
        "ADM", 2022, "publicado", [9, 1], 1,
        "Estudo de caso com lojistas que passaram a vender por canais digitais, avaliando custos, vendas e dificuldades de adoção.",
    ),
    (
        "Indicadores de sustentabilidade em empresas do setor têxtil",
        "ADM", 2023, "publicado", [12, 9], 1,
        "Levantamento de indicadores ambientais e sociais publicados por indústrias têxteis e discussão de sua comparabilidade.",
    ),
    (
        "Segurança da informação em escritórios de contabilidade",
        "ADM", 2024, "publicado", [4, 9], 1,
        "Diagnóstico das práticas de proteção de dados de clientes em escritórios de pequeno porte e proposta de plano de adequação à LGPD.",
    ),
    (
        "Análise de dados de vendas para tomada de decisão no varejo",
        "ADM", 2025, "publicado", [13, 9], 1,
        "Uso de análise exploratória sobre séries de vendas para apoiar decisões de estoque e promoções em uma rede de supermercados.",
    ),
    (
        "Governança de dados em organizações públicas",
        "ADM", 2026, "em_andamento", [3, 9], 1,
        "Revisão de modelos de governança de dados e levantamento de práticas adotadas por órgãos municipais.",
    ),
]

USUARIOS = [
    ("coordenacao1", "coordenacao1@ifpb.edu.br", "Coord@2026-1"),
    ("coordenacao2", "coordenacao2@ifpb.edu.br", "Coord@2026-2"),
]
