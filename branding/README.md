# Robert Tv — logo escolhida pelo usuário

Os arquivos fornecidos em `Downloads/Robert_TV_vetorial_claro_escuro`
foram copiados integralmente para `originals/`, incluindo o LEIA-ME e os PNGs.
Esses originais são a fonte da identidade visual e não são redesenhados pelo script.

- `originals/Robert_TV_claro.svg`: marca para fundo claro.
- `originals/Robert_TV_escuro.svg`: marca para fundo escuro.
- `originals/Robert_TV_simbolo.svg`: símbolo isolado.
- `robert-tv.svg` e `robert-tv-transparent.svg`: cópias da marca clara transparente.
- `robert-tv-dark.svg`: cópia da marca escura transparente.
- `robert-tv-mark.svg`: cópia do símbolo.
- `robert-tv-square.svg`: composição quadrada com os mesmos caminhos e gradientes,
  símbolo acima do nome em branco, usando a versão escura fornecida sobre
  fundo grafite `#141419`, sem esticar a arte horizontal.
- `../tizen/robert-tv.png`: ícone 1024 × 1024 renderizado diretamente do vetor,
  referenciado pelo manifesto Tizen.

Regenerar com `python3 branding/build_brand.py` (Python 3 e rsvg-convert).
Os SVGs fornecidos têm letras em curvas e não exigem fontes instaladas.
A origem descrita pelo fornecedor está em `originals/LEIA-ME.txt`.

A marca anterior criada pelo assistente foi substituída pela escolha do usuário.
O tamanho externo do bloco no Smart Hub é controlado pela Samsung.
O nome do app continua Robert Tv; seu ID técnico e certificado são preservados.

Diagnóstico na UN50NU7100 (23/10/2026): o ícone instalado em
`/opt/usr/apps/FreeMyTVio/shared/res/FreeMyTVio.FreeMyTV.png` foi lido pelo
Web Inspector. Na versão 1.1.3, suas dimensões eram 512 × 512 e seus pixels
eram idênticos aos do PNG enviado. Não houve redução para 117 × 117 durante
a instalação. A resolução interna do desenho/cache do Smart Hub não foi
medida. A versão 1.1.4 testa PNG 1024 × 1024; melhora visual ainda depende
da comparação na TV e não deve ser declarada apenas pela instalação.

Após a atualização, o Web Inspector confirmou versão 1.1.4 e ícone
instalado com dimensões 1024 × 1024. Isso confirma a preservação da
resolução do arquivo; não mede a renderização final do Smart Hub.

A versão 1.1.5 testou 2048 × 2048. O usuário preferiu o resultado anterior;
a versão 1.1.6 retorna a 1024 × 1024, mantendo a mesma composição.
