# Free My TV — versão pessoal

## Nome e marca: Robert Tv

O aplicativo Tizen passou a se chamar **Robert Tv**, versão local 1.1.10.
O nome é definido em `tizen/config.xml` e no título de `web/index.html`.
O ID técnico e a assinatura foram mantidos para preservar a instalação,
as preferências e os atalhos. O projeto original continua creditado.

A marca vetorial está em `branding/`. O pacote usa o ícone quadrado
`tizen/robert-tv.png` (1024 × 1024), gerado de `branding/robert-tv-square.svg`.
A identidade usa a logo vetorial escolhida pelo usuário, preservada em
`branding/originals/`, com versões clara, escura e símbolo em degradê.
O ícone quadrado reorganiza os caminhos originais sem distorcer a marca,
com nome branco e fundo grafite `#141419`, conforme ajuste solicitado na TV.

Após aprovação da prévia pelo usuário, o cabeçalho usa a logo no lugar de
“Para você”, com 430 × 110 pixels em x=76, y=34. Os SVGs transparentes em
`web/icons/robert-tv-light.svg` e `robert-tv-dark.svg` alternam pela classe
`.night` já usada pelo tema. A marca permanece após reabrir o app e trocar
o idioma, preservando a navegação e o espaçamento das abas.
O tamanho externo e o destaque do cartão do Smart Hub continuam sujeitos
ao sistema Samsung. Não confundir dimensões do arquivo com as do cartão.

O controle Android mantém o nome Minha TV; seu atalho para o aplicativo da TV
foi atualizado para Robert Tv no APK 1.2, sem trocar o ID do destino.

Repositório original: https://github.com/simbasjungles/free-my-tv

## Correção para Samsung UN50NU7100

O atalho da Netflix da loja (`RN1MCdNq8t.Netflix`) apresentou tela preta.
O teste na TV confirmou que `org.tizen.netflix-app` abre normalmente.
`web/tv.js` agora prefere a Netflix nativa quando ela existe. Se não existir,
mantém o aplicativo da loja. A mudança vale também para atalhos já salvos.

O YouTube da loja (`9Ur5IzDKqV.TizenYouTube`) também é direcionado ao nativo
`com.samsung.tv.cobalt-yt`, quando disponível. O usuário confirmou na TV que
esse caminho abre com sua conta já conectada. YouTube Kids não é alterado.

Validação local:

```bash
node tests/samsung-netflix.cjs
bash tools/check.sh web
python3 tizen/build.py --generic --preview
```

O pacote gerado é `FreeMyTV-tizen.wgt`. O build acima não assina o pacote.
A versão instalada anteriormente veio da release original assinada; uma
atualização com outro certificado pode exigir remover somente o Free My TV
antes de instalar a versão pessoal, perdendo as preferências desse aplicativo.
Não remover a Netflix nem outros aplicativos da TV.

## Personalização visual futura

- `web/home.css`: cores, tamanhos, espaçamentos e aparência.
- `web/home.js`: navegação, composição e comportamento da interface.
- `web/index.html`: estrutura da tela.
- `web/icons/`: ícones e logos.
- `out/tizen/index.html`: prévia gerada; editar os arquivos de `web/`.

Manter JavaScript ES5 e as limitações de CSS descritas em `CLAUDE.md`, pois
o navegador da TV é antigo. A interface visual ainda não foi modificada.

Manter a tela inicial Samsung e o início automático como estão. Este projeto
é um aplicativo removível; não exige alteração de firmware.

## Teste de retomada solicitado pelo usuário

Em 23/10/2026, foi testado `background-support="enable"` para tentar a
retomada automática. **O teste falhou.** O comando Power enviado pelo agente
não desligou a TV; o próprio usuário fez o ciclo normal de desligar/ligar e
confirmou que o Free My TV não iniciou automaticamente.

A alteração de segundo plano e o registro experimental de eventos foram
retirados. Não declarar que o agente desligou/ligou a TV nem que o recurso
funciona neste modelo. O manifesto voltou a `background-support="disable"`.

Não houve alteração no launcher nativo, firmware, contas ou preferências
de aplicativos. Registro detalhado: arquivo local
`../samsung-smart-hub/teste-retomada-free-my-tv.json`.

## Tela minimalista

Configurações → Mostrar recomendações (ativada por padrão). Desativar
esconde cards, abas e cotações do topo, mostra relógio e data, mantém
logo, barra de apps e botões de TV/entradas/configurações. A escolha
`recommendations` é salva nas preferências locais. A navegação por setas
pula as abas escondidas. Reativar restaura as recomendações.

Na versão 1.1.9, relógio e data ficam centralizados na área livre entre o
cabeçalho e a barra, apenas no modo minimalista.

## Localização da previsão

Cidade informada pelo usuário: Aparecida do Taboado, MS. O arquivo privado
`config.properties` usa latitude -20.086944 e longitude -51.093889.
Coordenadas de referência: IBGE, Nomes Geográficos da BCIM,
https://biblioteca.ibge.gov.br/visualizacao/livros/liv56282.pdf.

Consulta na própria UN50NU7100: as capacidades `location`, `location.gps`
e `location.wps` retornam false. O fuso `America/Campo_Grande` não estabelece
a cidade real. Não afirmar que a previsão acompanha mudanças de endereço;
a cidade foi configurada explicitamente. O cache do clima já é separado
pelas coordenadas, então os dados antigos não são reaproveitados para ela.

Na versão 1.1.10, a pedido do usuário, relógio e data voltam à posição
original à esquerda também no modo minimalista. A cidade permanece Aparecida do Taboado.
