import random



######################################################
                       #Genes
######################################################

def gene_cb():
    '''Gera um gene válido para o problema das caixas binárias.
    
    Return:
        Um valor zero ou um.
    '''
    
    
    gene_aceitavel = [0,1] #lista com valores aceitáveis de gene
    gene_aleatorio = random.choice(gene_aceitavel) #escolhe um valor aleatório da lista de gene_aceitavel
    return gene_aleatorio #retorna o valor aleatório escolhido

def gene_cnb(valor_max_caixa):
    '''Gera um gene válido para o problema das caixas não binárias
    
    Args:
        valor_max_caixa: Valor máximo que a caixa pode assumir.
    
    Return:
        Um valor zero a 'valor_max_caixa' (incluso)
    '''
    
    gene_aleatorio = random.randint(0,valor_max_caixa) #escolhe aleatório de 0 até 'valor_max_caixa'
    return gene_aleatorio #retorna um gene aleatório válio

def gene_letra(letras):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras) #seleciona aleatoriamente uma letra do input 
    return letra

######################################################
                       #Individuo
######################################################

    
def individuo_cb(n):
    '''Gera um indivíduo das caixas binárias.
    
    Args:
        n: número de genes do indivíduo
    
    Return:
        Uma lista de genes, de modo que os valores aceitos são 0 e 1.
    '''
    individuo = []
    for i in range(0,n,1): #repete as funções n vezes
        gene = gene_cb() #retorna um gene aleatório
        individuo.append(gene) #armazena o gene em uma lista
    return individuo #retorna uma lista com len == 4

def individuo_cnb(numero_genes,valor_max_caixa):
    '''Gera um indivíduo válido para o problema de caixas não binárias
    Args:
        numero_genes: númreo de genes da lista
        valor_max_caixa: Valor máximo que a caixa pode assumir.
        
    Return: lista que representa um indivíduo
    '''
    
    individuo = []
    for _ in range(0,numero_genes,1): #repete as funções n vezes
        gene = gene_cnb(valor_max_caixa) #retorna um gene aleatório
        individuo.append(gene) #armazena o gene em uma lista
    return individuo #retorna uma lista com len == 4


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Return:
      Lista com n letras
    """

    candidato = [] #lista com o candidato

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras)) #cria um individuo com um len == n

    return candidato

######################################################
                       #População
######################################################

def populacao_cb(tamanho,genes):
    '''Cria uma população no problema das caixas binárias.
    
    Returns:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista (ou um conjunto de listas) com "n" genes.
    
    Args:
        tamanho: tamanho da população
        genes: quantidade de genes
    '''
    populacao = []
    for _ in range(0,tamanho,1): #usar "_" apenas para a situação de não precisar do valor do "for"
        populacao.append(individuo_cb(genes))
    return populacao

def populacao_cnb(tamanho,genes,valor_max_caixa):
    
    '''Cria uma população no problema das caixas não binárias.
    
    Returns:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista (ou um conjunto de listas) com "n" genes.
    
    Args:
        tamanho: tamanho da população
        genes: quantidade de genes
        valor_max_caixa: Valor máximo que a caixa pode assumir.
    '''
    populacao = []
    for _ in range(0,tamanho,1): #usar "_" apenas para a situação de não precisar do valor do "for"
        populacao.append(individuo_cnb(genes,valor_max_caixa))
    return populacao



def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha

    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras)) #cria uma lista de listas como populacao (senhas)
    return populacao


######################################################
              #Função Objetivo/Fitness - individuo
######################################################

def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.        
    Args:      
        individuo: lista contendo os genes das caixas binárias.        
    
    Return:      
        Um valor representando a soma dos genes do indivíduo.    
    """
    return sum(individuo)

def funcao_objetivo_cnb(individuo):
    """Computa a função objetivo no problema das caixas não binárias.        
    Args:      
        individuo: lista contendo os genes das caixas não binárias.        
    
    Return:      
        Um valor representando a soma dos genes do indivíduo (fitness).    
    """
    fitness =  sum(individuo) #fintess
    return fitness


def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha

    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira): #corre duas listas ao mesmo tempo
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial)) #determina a diferenca pelo valor abs

    return diferenca


######################################################
              #Função Objetivo/Fitness - populacao
######################################################


def funcao_objetivo_pop_cb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população
    
        Args:     
            populacao: lista com todos os indivíduos da população       
        
        Return:      
            Lista de valores representando a fitness de cada indivíduo de uma população.    
        
        """    
    
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness


def funcao_objetivo_pop_cnb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população
    
        Args:     
            populacao: lista com todos os indivíduos da população       
        
        Return:      
            Lista de valores representando a fitness de cada indivíduo de uma população.    
        
        """    
    
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop



def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira)) #determina o fitness por individuo e armazena

    return resultado

######################################################
                       #Seleção
######################################################


def selecao_roleta_max(populacao, fitness):
    '''Seleciona individuos de uma população usando o método da roleta.
    
    Nota: funciona apenas para problemas de maximização.
    Nota_2: retorna uma população de mesmo tamanho do input.
    
    Return: 
        População dos indivíduos selecionados
    
    Args:
        populacao: lista com todos os individuos da populacao
        fitness: lista com o valor da funcao objetivo dos individuos da populcao
    
    '''
    
    populacao_selecionada = random.choices(populacao, weights=fitness,k=len(populacao)) #escolher com pesos
    return populacao_selecionada
    

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: população do problema
      fitness: lista de fitness
      tamanho_torneio: quantidade de invidiuos que batalham entre si

    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados

######################################################
                       #Cruzamento
######################################################  
    
def cruzamento_ponto_simples(pai,mae):
    '''Operador de cruzamento de ponto simples.
    
    Args:
        pai: uma lista representando um indivíduo
        mãe: uma lista representando um indivíduo
    
    Return:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos
    '''
    
    ponto_de_corte = random.randint(1, ((len(pai))-1)) #na lista
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
#filho1: pega todos os genes do pai até 'ponto_de_corte', concatena com todos os genes da mãe, menos "ponto_de_corte"
#filho2: pega todos os genes do mãe até 'ponto_de_corte', concatena com todos os genes da pai, menos "ponto_de_corte"
    
    return filho1,filho2

######################################################
                       #Mutação
######################################################

def mutacao_cb(individuo):
    '''Realiza a mutação de um gene no problema das caixas binárias
    
    Args:
        individuo: uma lista representado um individuo no papel das caixas vinárias
    
    Return:
        Um indivíduo com um gene mutado
    
    '''
    
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb() #substitui o gene mutado por algum gene aleatorio
    return individuo

def mutacao_cnb(individuo,valor_max_caixa):
    '''Realiza a mutação de um gene no problema das caixas binárias
    
    Args:
        individuo: uma lista representado um individuo no papel das caixas vinárias
    
    Return:
        Um indivíduo com um gene mutado
    
    '''
    
    gene_a_ser_mutado = random.randint(0, len(individuo)-1) #gera um index aleatório
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa) #altera um valor em um indivíduo (índex aleatório)
    return individuo


def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.

    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.

    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras) #altera um gene aleatorio no index "gene" por um gene aleatorio
    return individuo

    
