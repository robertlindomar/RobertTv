# Free My TV — versão pessoal

Repositório original: https://github.com/simbasjungles/free-my-tv

## Correção para Samsung UN50NU7100

O atalho da Netflix da loja (`RN1MCdNq8t.Netflix`) apresentou tela preta.
O teste na TV confirmou que `org.tizen.netflix-app` abre normalmente.
`web/tv.js` agora prefere a Netflix nativa quando ela existe. Se não existir,
mantém o aplicativo da loja. A mudança vale também para atalhos já salvos.

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
