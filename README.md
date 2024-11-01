
# Verificação de Preços de Tênis Nike Air Max Excee

Este projeto usa `Selenium` e Python para monitorar preços de um modelo de tênis Nike em três sites diferentes: Centauro, Nike e Mercado Livre. Ele captura os preços dos produtos e os registra em um arquivo de log (`precos_log.txt`).

## Requisitos

- Python 3.7+
- Google Chrome (atualizado)
- ChromeDriver (compatível com a versão do Chrome instalada)
- Dependências do Python: `selenium`, `re`, `logging`, `time`

## Instalação

1. **Clone este repositório**:

    ```bash
    git clone https://github.com/seu_usuario/verificacao_precos.git
    cd verificacao_precos
    ```

2. **Instale as dependências do Python**:

    ```bash
    pip install selenium
    ```

3. **Baixe o ChromeDriver**:

    - Baixe o [ChromeDriver](https://sites.google.com/chromium.org/driver/) que corresponde à versão do Google Chrome instalada no seu sistema.
    - Extraia o executável e mova-o para uma pasta incluída no seu PATH, ou coloque-o na raiz do projeto.

## Uso

1. **Configuração do arquivo de log**:

    O script salva os logs em `logs/precos_log.txt`. Se a pasta `logs` não existir, crie-a manualmente:

    ```bash
    mkdir logs
    ```

2. **Executando o script**:

    Para iniciar o monitoramento de preços, execute o script `verificar_precos.py`:

    ```bash
    python verificar_precos.py
    ```

    O script irá:

    - Acessar cada site (Centauro, Nike e Mercado Livre).
    - Capturar o preço do produto e formatá-lo.
    - Registrar os preços encontrados no console e em `logs/precos_log.txt`.

3. **Interrompendo o script**:

    Para interromper o script manualmente, pressione `Ctrl + C` no terminal. Isso irá parar a execução e salvar uma mensagem de interrupção no arquivo de log.

## Estrutura do Código

- `configurar_driver()`: Configura o WebDriver com um User-Agent personalizado.
- `verificar_precos(driver)`: Verifica os preços nos sites Centauro, Nike e Mercado Livre.
- `Loop de verificação`: Executa a verificação de preços a cada 1 minuto.

## Exemplo de Log

O arquivo `precos_log.txt` será atualizado com informações sobre preços como este exemplo:

```text
2024-10-31 12:00:00 - Preços encontrados: {'Centauro': 'R$ 549,47', 'Nike': 'R$ 599,99', 'Mercado Livre': 'R$ 679,00'}
2024-10-31 12:01:00 - Preços encontrados: {'Centauro': 'R$ 549,47', 'Nike': 'R$ 599,99', 'Mercado Livre': 'R$ 679,00'}
```

## Observações

- **Compatibilidade com o Chrome**: Verifique se a versão do ChromeDriver corresponde à versão do Google Chrome instalada no seu sistema.
- **Intervalo de atualização**: O script atualmente atualiza os preços a cada 1 minuto (`time.sleep(60)`). Você pode ajustar esse valor conforme necessário.
- **Erro de Elemento**: Se algum dos sites atualizar sua estrutura, o seletor CSS pode precisar ser ajustado no código.

## Problemas Conhecidos

- Alguns sites podem bloquear o acesso automatizado. Nesse caso, considere ajustar o User-Agent ou usar um intervalo maior entre as verificações.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
