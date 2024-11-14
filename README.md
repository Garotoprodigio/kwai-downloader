
# Kwai Video Downloader

Este script em Python utiliza Selenium para automatizar o download de vídeos de um perfil público do Kwai com base em um número mínimo de "likes". Ele percorre a página de perfil, encontra os vídeos que atendem aos critérios definidos e faz o download dos arquivos de vídeo em formato `.mp4`.

## Requisitos

- **Python 3.x**: Certifique-se de ter o Python 3.x instalado.
- **Bibliotecas Python**: Instale as bibliotecas necessárias com o seguinte comando:

  ```bash
  pip install requests selenium webdriver-manager
  ```

- **Chromedriver**: Este script usa o `webdriver_manager` para instalar e configurar automaticamente o Chromedriver.

## Configurações

Antes de executar o script, personalize os seguintes parâmetros no código:

- **`profile_url`**: URL do perfil do Kwai (exemplo: `https://www.kwai.com/@Portelas`).
- **`min_likes`**: Número mínimo de likes para que o vídeo seja baixado.
- **`max_videos`**: Número máximo de vídeos que deseja baixar.

## Como Executar

1. Certifique-se de que todos os requisitos foram instalados.
2. Execute o script no terminal com:

   ```bash
   python kwai_downloader.py
   ```

3. O script acessará o perfil do Kwai, rolará a página para carregar os vídeos e fará o download dos vídeos que atendem ao mínimo de likes especificado.

## Observações

- **Execução em Modo Headless**: O script executa o navegador em modo "headless" (sem abrir a janela do navegador) para melhor desempenho.
- **Downloads Limitados**: Para evitar que o Kwai detecte comportamento automatizado, o script está configurado para rolar a página gradualmente e aguardar o carregamento de novos conteúdos.
- **Estrutura de Arquivo**: Os vídeos são salvos na pasta onde o script está localizado, com nomes como `video_1.mp4`, `video_2.mp4`, etc.

## Exemplo de Saída

```plaintext
Vídeo 1 baixado com sucesso: [URL do vídeo]
Vídeo 2 baixado com sucesso: [URL do vídeo]
...
Download concluído.
```

## Problemas Comuns

- **Bloqueio de Acesso**: Kwai pode bloquear o acesso se perceber que o perfil está sendo acessado de forma não natural. Ajuste o tempo de espera (`time.sleep()`) se necessário.
- **Elemento Não Encontrado**: Verifique se os seletores de elementos (como `By.XPATH`) correspondem ao layout atual do site Kwai.

## Licença

Este script é distribuído sob a licença MIT.
