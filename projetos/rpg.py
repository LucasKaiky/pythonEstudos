import numpy as np
import time
import sys
import random
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
class Pokemon:
    def __init__(self, nome, tipo, skills, evs, vida='===================='):
        self.nome = nome
        self.tipo = tipo
        self.skills = skills
        self.ataque = evs['ATAQUE']
        self.defesa = evs['DEFESA']
        self.vida = vida
        self.barras = 20
    
    def luta(self, Pokemon2):
        print('---LUTA ENTRE POKEMONS---')
        print(f'\n{self.nome}')
        print(f'TIPO/{self.tipo}')
        print(f'ATAQUE/{self.ataque}')
        print(f'DEFESA/{self.defesa}')
        print('LvL/', 3*(1+np.mean([self.ataque, self.defesa])))
        print('\nVS')
        print(f'\n{Pokemon2.nome}')
        print(f'TIPO/{Pokemon2.tipo}')
        print(f'ATAQUE/{Pokemon2.ataque}')
        print(f'DEFESA/{Pokemon2.defesa}')
        print(f'LvL/', 3*(1+np.mean([Pokemon2.ataque, Pokemon2.defesa])))
        time.sleep(2)
        
        tipos = ['Fogo', 'Água', 'Planta']
        for i,k in enumerate(tipos):
            if self.tipo == k:
                if Pokemon2.tipo == k:
                    string_1_ataque = '\nNão é muito efetivo...'
                    string_2_ataque = '\nNão é muito efetivo...'
            
                if Pokemon2.tipo == tipos[(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defesa *= 2
                    self.ataque /= 2
                    self.defesa /= 2
                    string_1_ataque = '\nNão é muito efetivo...'
                    string_2_ataque = '\nÉ muito efetivo!'

                if Pokemon2.tipo == tipos[(i+2)%3]:
                    self.ataque *= 2
                    self.ataque *= 2
                    Pokemon2.ataque /= 2
                    Pokemon2.defesa /= 2
                    string_1_ataque = '\nÉ muito efetivo!'
                    string_2_ataque = '\nNão é muito efetivo...'
                    
        while (self.barras > 0) and (Pokemon2.barras > 0):
            print(f'\n{self.nome}\t\tVIDA\t{self.vida}')
            print(f'\n{Pokemon2.nome}\t\tVIDA\t{Pokemon2.vida}')
            print(f'\nVAI {self.nome}!!!')
            for i,x in enumerate(self.skills):
                print(f'{i+1}.', x)
            index = int(input('Escolha uma skill: '))
            delay_print(f"\n{self.nome} usou {self.skills[index-1]}!")
            time.sleep(1)
            delay_print(string_1_ataque)
        
            Pokemon2.barras -= self.ataque
            Pokemon2.vida = ''
    
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defesa)):
                Pokemon2.vida += "="
    
            time.sleep(1)
            print(f'\n{self.nome}\t\tVIDA\t{self.vida}')
            print(f'\n{Pokemon2.nome}\t\tVIDA\t{Pokemon2.vida}')
            time.sleep(.5)
           
            if Pokemon2.barras <= 0:
                delay_print(f'\n...{Pokemon2.nome} foi derrotado!')
                break
                
                
            print(f'\nVAI {Pokemon2.nome}!!!')
            for i,x in enumerate(Pokemon2.skills):
                print(f'{i+1}.', x)
            index = int(input('Escolha uma skill: '))
            delay_print(f"\n{Pokemon2.nome} usou {Pokemon2.skills[index-1]}!")
            time.sleep(1)
            delay_print(string_2_ataque)
        
            self.barras -= Pokemon2.ataque
            self.vida = ''
    
            for j in range(int(self.barras+.1*self.defesa)):
                self.vida += "="
    
            time.sleep(1)
            print(f'\n{self.nome}\t\tVIDA\t{self.vida}')
            print(f'\n{Pokemon2.nome}\t\tVIDA\t{Pokemon2.vida}')
            time.sleep(.5)
    
            if self.barras <= 0:
                delay_print(f'\n... {self.nome} foi derrotado!')
                break
                
                
                    

            
if __name__ == '__main__':
    Charizard = Pokemon('Charizard', 'Fogo', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATAQUE':12, 'DEFESA': 8})
    Blastoise = Pokemon('Blastoise', 'Água', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATAQUE': 10, 'DEFESA':10})
    Venusaur = Pokemon('Venusaur', 'Planta', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATAQUE':8, 'DEFESA':12})

    Charmander = Pokemon('Charmander', 'Fogo', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATAQUE':4, 'DEFESA':2})
    Squirtle = Pokemon('Squirtle', 'Água', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATAQUE': 3, 'DEFESA':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Planta', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATAQUE':2, 'DEFESA':4})

    Charmeleon = Pokemon('Charmeleon', 'Fogo', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATAQUE':6, 'DEFESA':5})
    Wartortle = Pokemon('Wartortle', 'Água', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATAQUE': 5, 'DEFESA':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Planta', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATAQUE':4, 'DEFESA':6})
listaPokemons = [Charmander, Squirtle, Bulbasaur, Charmeleon, Wartortle, Ivysaur, Charizard, Blastoise, Venusaur]

while True:
        pokemonInicial = int(input('Escolha seu pokemon inicial: 1 - Charmander, 2 - Squirtle, \n3 - Bulbasaur, 4 - Charmeleon, 5 - Wartortle, 6 - Ivysaur, \n7 - Charizard, 8 - Blastoise ou 9 - Venusaur? '))
        if pokemonInicial == 1:
            pokemonInicial = Charmander
        if pokemonInicial == 2:
            pokemonInicial = Squirtle
        if pokemonInicial == 3:
            pokemonInicial = Bulbasaur
        if pokemonInicial == 4:
            pokemonInicial = Charmeleon
        if pokemonInicial == 5:
            pokemonInicial = Wartortle
        if pokemonInicial == 6:
            pokemonInicial = Ivysaur
        if pokemonInicial == 7:
            pokemonInicial = Charizard
        if pokemonInicial == 8:
            pokemonInicial = Blastoise
        if pokemonInicial == 9:
            pokemonInicial = Venusaur
        pokemonInicial.luta(random.choice(listaPokemons))   
        escolha = str(input('Deseja Batalhar [S/N]? ')).strip().upper()
        if escolha == 'N':
            break

    
#by LucasKaiky :P          