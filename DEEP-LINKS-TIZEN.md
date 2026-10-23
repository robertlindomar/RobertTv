# Investigação de links para títulos na Samsung UN50NU7100

## Estado confirmado

- TMDB está configurado apenas no arquivo local ignorado `config.properties`.
- Cards e imagens de Explorar, Filmes e Séries carregam em português, região BR.
- O clique atual em um card chama somente o aplicativo do serviço.
- `web/home.js` não passa o ID do título no clique. O caminho Samsung de
  `TV.launch` em `web/tv.js` também não usa `params`.
- A integração Watchmode em `app/src/io/freemytv/Recs.java` pertence à versão
  Android. Ela não está implementada em `web/data.js` nem no build Tizen.

## Testes apenas em tempo de execução

1. `launchAppControl` com operação `view`, URI HTTPS de Masterplan e destino
   `evKhCgZelL.AmazonIgnitionLauncher2`: o usuário mostrou o seletor de perfis
   do Prime. Isso não confirmou a abertura do título.
2. Enviado `KEY_ENTER` uma vez para o perfil Robert destacado na foto.
3. Enviado `launchAppControl` com operação `default` ao aplicativo nativo
   `org.tizen.ignition` e `ApplicationControlData` com chave `PAYLOAD`.
   O campo `values` foi uma string JSON contendo `contentId`, `url` e
   `action: detail`, para Masterplan. Esses campos internos são uma hipótese
   para teste: o formato específico aceito pelo Prime não foi confirmado.
   Nenhuma alteração desse teste foi incorporada ao pacote instalado.

Título usado no teste: Masterplan, ID Prime Video `0K2MF62NJL76Q54YS0KEABBDVZ`.
Página oficial: https://www.primevideo.com/detail/0K2MF62NJL76Q54YS0KEABBDVZ

## Limites da verificação

O endpoint Samsung de aplicativos fornece estado de execução/visibilidade,
mas não informa qual título está na tela. `accepted`, `running` ou `visible`
não demonstram que um link abriu a página do filme. A inspeção do Prime pelo
comando SDB `debug` foi recusada pela TV. Não afirmar sucesso sem observar
o destino do link. Não automatizar OK repetidamente: poderia iniciar reprodução
ou confirmar uma compra quando o foco fosse outro.

Preservar perfis, contas, configurações e aplicativos nativos. Não solicitar
fotos a cada tentativa; consolidar o diagnóstico e pedir confirmação visual
somente quando indispensável. Não prometer que outra chave de API resolve
o formato de abertura aceito pelo Prime.

## Documentação

- Samsung, AppControl e PAYLOAD de previews:
  https://developer.samsung.com/smarttv/develop/guides/smart-hub-preview/implementing-public-preview.html
- Samsung, Application API:
  https://developer.samsung.com/smarttv/develop/api-references/tizen-web-device-api-references/application-api.html
