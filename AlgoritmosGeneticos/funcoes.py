import random

def gene_cb():
    '''Gera um gene válido para o problema
    
    Return:
        Um valor zero ou um.
    '''
    
    
    gene_aceitavel = [0,1] #lista com valores aceitáveis de gene
    gene_aleatorio = random.choice(gene_aceitavel) #escolhe um valor aleatório da lista de gene_aceitavel
    return gene_aleatorio #retorna o valor aleatório escolhido
    
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

def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.        
    Args:      
        individuo: lista contendo os genes das caixas binárias.        
    
    Return:      
        Um valor representando a soma dos genes do indivíduo.    
    """
    return sum(individuo)

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

def mutacao_cb(individuo):
    '''Realiza a mutação de um gene no problema das caixas binárias
    
    Args:
        individuo: uma lista representado um individuo no papel das caixas vinárias
    
    Return:
        Um indivíduo com um gene mutado
    
    '''
    
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo

