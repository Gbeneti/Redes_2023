import random

###############################################################################
#                                   Suporte                                   #
##############################################################################+


# NOVIDADE
def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.

    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) #calcula a distância euclidiana

    return dist


def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.

    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random()) #cria um dicionário com as cidades {nome:coordenada}

    return cidades

# NOVIDADE
def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila

    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    valor_total = 0
    peso_total = 0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]['valor'] #pega o valor de 'valor' do item no dicionario de dicionarios
            peso_do_item = objetos[nome_do_item]['peso'] #pega o valor de 'peso' do item no dicionario de dicionarios
            
            valor_total += valor_do_item
            peso_total += peso_do_item

    return valor_total, peso_total


###############################################################################
#                                    Genes                                    #
###############################################################################


def gene_cb():
    """Gera um gene válido para o problema das caixas binárias

    Return:
      Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista) #escolhe um gene binário
    return gene


def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias

    Args:
      valor_max_caixa: número inteiro representando o maior valor possível que
      pode existir dentro de uma caixa.

    Return:
      Um valor entre zero a `valor_max_caixa` (inclusive).
    """
    gene = random.randint(0, valor_max_caixa) #escolhe um gene no range de input
    return gene


def gene_letra(letras):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras) #escolhe uma das letras possíveis
    return letra

###############################################################################
#                                  Indivíduos                                 #
###############################################################################


def individuo_cb(n):
    """Gera um individuo para o problema das caixas binárias.

    Args:
      n: número de genes do indivíduo.

    Return:
       Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb() #escolhe um gene
        individuo.append(gene) #armazena o gene
    return individuo


def individuo_cnb(n_genes, valor_max_caixa):
    """Gera um individuo para o problema das caixas não-binárias.

    Args:
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa

    Return:
       Uma lista com n genes. Cada gene é um valor entre zero e
       `valor_max_caixa`.
    """
    individuo = []
    for i in range(n_genes):
        gene = gene_cnb(valor_max_caixa) #escolhe o gene
        individuo.append(gene) #armazena o gene
    return individuo


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras)) #cria e armazena o gene

    return candidato


def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys()) #lista as chaves do dicinário (nome das cidades)
    random.shuffle(nomes) #embaralha a lista 'nomes'
    return nomes


def individuo_palindromo(tamanho_palindromo, letras): #pode ser substiuído pelo da senha
    '''Gera um candidato para o problema dos palindromos.
    
    Args:
        tamanho_palindromo: valor que relresenta o numero de genes do palindromo
        letras: letras que podem ser genes
    
    Return:
        Uma lista de genes, de modo que os caracteres aceitos estão na lista "letras" 
    '''

    candidato = [] #lista com o candidato

    for n in range(tamanho_palindromo):
        candidato.append(gene_letra(letras)) #cria um individuo com 'n' genes
    return candidato


###############################################################################
#                                  População                                  #
###############################################################################


def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.

    Args:
      tamanho: tamanho da população.
      n: número de genes do indivíduo.

    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com `n`
      genes.
    """
    populacao = []
    for _ in range(tamanho): #'_' usado pois o valor do 'for' não será armazenado
        populacao.append(individuo_cb(n)) #cria e armazena um indiviuo
    return populacao


def populacao_cnb(tamanho, n_genes, valor_max_caixa):
    """Cria uma população no problema das caixas não-binárias.

    Args:
      tamanho: tamanho da população.
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa

    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com
      `n_genes` genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n_genes, valor_max_caixa)) #cria e armazena um individuo
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
    for _ in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras)) #cria e armazena um individuo
    return populacao



def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.

    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades)) #cria e armazena um individuo
    return populacao

def populacao_inicial_palindromo(tamanho, tamanho_palindromo, letras): 
    """Cria população inicial no problema do palindromo

    Args
      tamanho: tamanho da população.
      tamanho_palindromo: inteiro representando o tamanho do individuo.
      letras: letras possíveis de serem sorteadas.

    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_palindromo(tamanho_palindromo, letras)) #cria uma lista de listas como populacao
    return populacao



###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_roleta_max(populacao, fitness):
    """Seleciona individuos de uma população usando o método da roleta.

    Nota: apenas funciona para problemas de maximização.

    Args:
      populacao: lista com todos os individuos da população
      fitness: lista com o valor da funcao objetivo dos individuos da população

    Returns:
      População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(
        populacao, weights=fitness, k=len(populacao) #escolhe 'k' individuos da populacao para alcular fitness
    )
    return populacao_selecionada


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos da população
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
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio) #escolhe 'tamanho_torneio' individuos

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0] #entrega o individuo correspondente
            fit = par_individuo_fitness[1] #entrega o fitness correspondente

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit #atualiza a variavel 'fit' para encontrar um novo mínimo

        selecionados.append(selecionado) #armazena o individuo selecionado (com menor fitness)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1) #escolhe o ponto de corte, não pode ser em [0] e nem [-1]

    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:] #[p:q] -> p é inclusivo e q é exclusivo
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:] #assim, 'mae[#]' e pai[#] são sempre complementares

    return filho1, filho2


def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.

    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.

    Ver pág. 37 do livro do Wirsansky.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = random.randint(0, len(pai) - 2) #determina onde será o corte1
    corte2 = random.randint(corte1 + 1, len(pai) - 1) #determina onde será o corte2
    
    filho1 = pai[corte1:corte2] #varre de 'corte1' até 'corte2' (exclui corte2)
    for gene in mae:
        if gene not in filho1: #verifica os genes que não estão presentes com base no outro parente
            filho1.append(gene) #armazena os genes não presentes
            
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
            
    return filho1, filho2


###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias

    Args:
      individuo: uma lista representado um individuo no problema das caixas
      binárias

    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1) #escolhe um local aleatorio
    individuo[gene_a_ser_mutado] = gene_cb() #substitui um gene aletorio no local selecionado
    return individuo


def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene no problema das caixas não-binárias

    Args:
      individuo:
        uma lista representado um individuo no problema das caixas não-binárias
      valor_max_caixa:
        maior número inteiro possível dentro de uma caixa

    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1) #escolhe um local aleatorio
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa) #substitui um gene aletorio no local selecionado
    return individuo


def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.

    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.

    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1) #escolhe um local aleatorio
    individuo[gene] = gene_letra(letras) #substitui um gene aletorio no local selecionado
    return individuo


def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.

    Args:
      individuo: uma lista representado um individuo.

    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    
    indices = list(range(len(individuo))) #lista com os ranges do individuo
    lista_sorteada = random.sample(indices, k=2) #sorteia 2 indices
    
    indice1 = lista_sorteada[0] #extrai o indice
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1] #inverte os indices de lugar - 'swap'
    
    return individuo

def mutacao_espelhada_palindromo(individuo, letras): 
    """Realiza a mutação de genes em indexes simétricos no problema dos palindromos.
       Utiliza a ideia de simetria presente na matemática, química e física.
       
       Nota: até onde se foi testado, funciona para individuos de tamanho par e ímpar. Quaisquer tamanhos.

    Args:
      individuo: uma lista representado um individuo no problema dos palindromos.
      letras: letras/genes possíveis de serem sorteadas.

    Return:
      Um individuo (palindromo) com dois genes iguais em index simetrico (mutado).
    """
    
    metade_quantidade_genes = (len(individuo) - 1) // 2 #metade do tamanho do individuo. Se impar, o valor é truncado
    gene = random.randint(0, metade_quantidade_genes) #valor aleatorio entre 0 e metade do tamanho do individuo
    
    individuo[gene] = gene_letra(letras) #substitui no index aleatoriamente selecionado
    individuo[- (gene + 1)] = individuo[gene] #substitui no index simetrico ao aleatoriamente selecionado
    return individuo

    
    


###############################################################################
#                         Função objetivo - indivíduos                        #
###############################################################################


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.

    Args:
      individiuo: lista contendo os genes das caixas binárias

    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo) #soma os valores contidos no individuo como genes


def funcao_objetivo_cnb(individuo):
    """Computa a função objetivo no problema das caixas não-binárias.

    Args:
      individiuo: lista contendo os genes das caixas não-binárias

    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo) #soma os valores contidos no individuo como genes


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

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial)) #converte string para valor numero e
                                                                               # computa a diferença
    return diferenca


def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.

    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
      
    Nota:
    Lembrar da estruturação de dados do individuo. O caminho de volta fará mais sentido então.
    """

    distancia = 0

    for posicao in range(len(individuo) - 1):
        
        partida = cidades[individuo[posicao]] #do dicionario cidade, extrai a posicao do individuo por index
        chegada = cidades[individuo[posicao + 1]] #chegada é um index maior do que partida
        
        percurso = distancia_entre_dois_pontos(partida, chegada) #computa a distancia euclidiana
        distancia = distancia + percurso #distancia total
               
    # Calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]

    percurso = distancia_entre_dois_pontos(partida, chegada) #computa a distancia euclidiana para retorno
    distancia = distancia + percurso #armazena a distancia de retorno
    
    return distancia

def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.

    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        valor_mochila = 0.01
        
    return valor_mochila



def funcao_objetivo_palindromo(individuo,vogais):
    """Computa a função objetivo no problema dos palindromos.        
    Args:      
        individuo: lista contendo caracteres.
        vogais: lista contendo vogais
    
    Return:      
        Um valor representando um "peso" (fitness) de quão próximo está o individuo de um palindromo.
    
    Nota: este é um algoritmo de minimização
    Nota_2: todo palindromo necessariamente precisa apresentar uma vogal.
    Nota_3: nesse algoritmo, pune-se (apenas) aqueles que não apresentam uma tendência desejável.
    Nota_4: não concede bonificações a aqueles que seguem uma tendência desejável.
    """
    fitness = 0
    individuo_reverso = individuo[::-1] #inverte a ordem do individuo
            
    for normal,inversa in zip(individuo,individuo_reverso):
        if normal != inversa:
            fitness += 500 #adição de fitness para aqueles que não apresentam letras iguais a inversa
    
     
    for i in vogais:
        if any(i in individuo for i in vogais): #se o individiuo apresenta pelo menos uma vogal
            fitness += 0
            return fitness
        else:
            fitness += 500 #caso não apresentar, punição
            return fitness
            
    return fitness


###############################################################################
#                         Função objetivo - população                         #
###############################################################################


def funcao_objetivo_pop_cb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população

    Args:
      populacao: lista com todos os individuos da população

    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo) #gera o fitness do individuo
        fitness.append(fobj) #armazena o fitness do individuo
    return fitness


def funcao_objetivo_pop_cnb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população

    Args:
      populacao: lista com todos os individuos da população

    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cnb(individuo) #gera o fitness do individuo
        fitness.append(fobj) #armazena o fitness do individuo
    return fitness


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
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira)) #gera e armazena o fitness do individuo

    return resultado


def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.

    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades)) #gera e armazena o fitness do indiviudo
    return resultado

# NOVIDADE
def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila

    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado


def funcao_objetivo_pop_palindromo(populacao,vogais):
    """Calcula a funcao objetivo para todos os membros de uma população
    
        Args:     
            populacao: lista com todos os indivíduos da população   
            vogais: letras requeridas para gerar o individuo
        
        Return:      
            Lista de valores representando a fitness de cada indivíduo de uma população.    
        
        """
    #print(populacao)
    fitness_pop = []
    for individuo in populacao:
        fitness_individuo = funcao_objetivo_palindromo(individuo, vogais) #gera o fitness do individuo
        
        fitness_pop.append(fitness_individuo) #armazena o fitness do individuo
    return fitness_pop
