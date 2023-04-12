# Unicode Normalization
Este programa tem a finalidade de normalizar uma string Unicode, removendo caracteres acentuados ou especiais e substituindo-os por caracteres básicos ASCII.
<br>

## Pré-requisitos
Python 3.x
<br>

## Como usar
Baixe o código ou clone o repositório.
Abra o arquivo unicode_normalization.py.
Execute o programa a partir da linha de comando com o comando python unicode_normalization.py.
Insira a string que você deseja normalizar.
<br>

### Exemplo

```bash
$ python unicode_normalization.py

Insira a string que deseja normalizar: ex: vários último peça

ex: vários último peça
```
<br>

## Como funciona
O programa utiliza a biblioteca unicodedata do Python para normalizar a string de entrada. Primeiro, ele utiliza a função normalize com o parâmetro "NFD" para decompor os caracteres acentuados ou especiais em caracteres básicos e seus diacríticos. Em seguida, ele remove esses diacríticos utilizando a função encode com o parâmetro "ascii" e o valor "ignore", que remove os caracteres desconhecidos. Por fim, a função decode é usada para converter a string resultante novamente em Unicode. Além disso, o programa também inclui uma função unicode que encapsula todo esse processo para facilitar a chamada a partir de outros programas.
<br>

## Contribuindo
Se você quiser contribuir para este projeto, sinta-se à vontade para criar um fork e enviar uma pull request com suas alterações.
<br>

## Licença
Este programa é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
