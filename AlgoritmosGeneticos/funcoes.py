def funcao_objetivo_cb(individuo):
    '''Computa a função objetivo no problema das caixas binárias.
    Args:
    individuo: lista contendo os genes das caixas binárias
    
    Return:
    Um valor representado a soma dos genes dos indivíduos.
    '''
    
    return sum(individuo) #soma os elementos da lista
     
