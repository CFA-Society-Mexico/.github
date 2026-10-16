# Cómo contribuir / Contributing

*English version [below](#english).*

## Español

Gracias por contribuir. Cualquier persona puede hacerlo: no necesitas ser miembro de CFA Society
México ni de la organización de GitHub.

### Qué puedes aportar

- Una herramienta nueva: calculadora, modelo, plugin, notebook o dataset público. Primero se
  propone; ver [Proponer un proyecto nuevo](#proponer-un-proyecto-nuevo).
- Mejoras a un proyecto existente: bugs, tests, documentación, traducciones.
- Ideas y preguntas en un [issue](https://github.com/CFA-Society-Mexico/.github/issues).

### Flujo para mejoras

1. Haz fork del repositorio.
2. Crea una rama: `git checkout -b mi-cambio`.
3. Haz tus cambios y commits.
4. Abre un pull request contra `main` y llena el checklist.
5. Un maintainer lo revisa; responde a sus comentarios.

### Requisito mínimo

Todo proyecto y todo PR debe cumplir:

1. **Licencia de código abierto** (recomendamos MIT) en un archivo `LICENSE`.
2. **Reproducible:** instrucciones de instalación y uso; sin datos ocultos ni rutas locales.
3. **Aviso legal:** indica que no es asesoría de inversión.
4. **Divulgación del uso de IA** en el README, con este formato:

```markdown
## Uso de IA / AI use
- Herramientas / Tools: <ej. Claude Code>
- Para qué / What for: <ej. código inicial y tests>
- Revisión humana / Human review: <quién revisó qué, ej. fórmulas verificadas contra Hull (2022)>
```

Además, sigue los principios de [IA responsable](RESPONSIBLE_AI.md): sin datos confidenciales y con
supuestos documentados.

### Proponer un proyecto nuevo

1. Abre un issue con el formulario
   [Proyecto nuevo](https://github.com/CFA-Society-Mexico/propuestas/issues/new?template=proyecto-nuevo.yml)
   en el repositorio [propuestas](https://github.com/CFA-Society-Mexico/propuestas). Si prefieres que tu agente de IA te entreviste y lo llene por ti, usa la skill
   [proponer-proyecto](https://github.com/CFA-Society-Mexico/propuestas/blob/main/skills/proponer-proyecto/SKILL.md).
2. El issue es público: no incluyas datos personales, de contacto, de clientes ni información
   confidencial. Abrirlo no implica aceptación, compromiso ni respaldo de CFA Society México ni de
   CFA Institute.
3. Los maintainers responden en el issue en un plazo estimado de 1 a 2 semanas; puede tardar más,
   porque revisamos como voluntarios. GitHub te avisa por correo.
4. Resultado: se hospeda en la organización (te damos permisos de administración), se lista en el
   perfil desde tu cuenta, se piden cambios o se cierra con un motivo breve basado en los criterios.

**Criterios de revisión**

1. Es relevante para la profesión financiera en México, Latinoamérica y otros países de habla
   hispana.
2. Cumple el [requisito mínimo](#requisito-mínimo).
3. No contiene datos confidenciales y declara cualquier relación comercial o con el empleador.
4. Tiene quién lo mantenga.
5. No duplica un proyecto existente.

Las ideas sin repositorio se revisan con menor prioridad que los proyectos en desarrollo o terminados.

**Si se publicó algo sensible por error**

1. Avisa a los maintainers en el mismo issue, sin repetir el dato, para que lo borren.
2. Si el dato quedó en el historial de ediciones, se pide a GitHub Support que lo purgue.
3. Si era una contraseña, token o llave, invalídala de inmediato: ya se considera comprometida.

### Aparecer en el perfil

Solo después de que tu propuesta sea aceptada:

1. Agrega a tu README el bloque de contribución comunitaria:

   ```markdown
   ## Contribución comunitaria / Community contribution
   - Autor / Author: <nombre, @usuario>
   - Propuesta aceptada / Accepted proposal: <link al issue>
   - La responsabilidad del contenido es del autor. Su inclusión no constituye respaldo, recomendación
     ni garantía de CFA Society México ni de CFA Institute. No es asesoría de inversión. / The author
     is responsible for the content. Its inclusion is not an endorsement, recommendation or guarantee
     by CFA Society México or CFA Institute. Not investment advice.
   ```

2. Abre un PR a este repositorio editando la tabla "Proyectos / Projects" de
   [`profile/README.md`](profile/README.md): una fila con área, enlace, descripción ES / EN y autor.
   Enlaza el issue aceptado en el PR.

### Código de conducta

Al participar aceptas el [Código de Conducta](CODE_OF_CONDUCT.md).

## English

Thank you for contributing. Anyone can: you do not need to be a member of CFA Society México or of
the GitHub organization.

### What you can contribute

- A new tool: calculator, model, plugin, notebook or public dataset. Propose it first; see
  [Propose a new project](#propose-a-new-project).
- Improvements to an existing project: bugs, tests, documentation, translations.
- Ideas and questions in an [issue](https://github.com/CFA-Society-Mexico/.github/issues).

### Flow for improvements

1. Fork the repository.
2. Create a branch: `git checkout -b my-change`.
3. Make your changes and commits.
4. Open a pull request against `main` and fill in the checklist.
5. A maintainer reviews it; respond to their comments.

### Minimum bar

Every project and every PR must have:

1. **An open-source license** (we recommend MIT) in a `LICENSE` file.
2. **Reproducibility:** setup and usage instructions; no hidden data or local paths.
3. **A disclaimer:** state that it is not investment advice.
4. **AI-use disclosure** in the README, in this format:

```markdown
## Uso de IA / AI use
- Herramientas / Tools: <e.g. Claude Code>
- Para qué / What for: <e.g. initial code and tests>
- Revisión humana / Human review: <who reviewed what, e.g. formulas checked against Hull (2022)>
```

Also follow the [responsible AI](RESPONSIBLE_AI.md) principles: no confidential data, documented
assumptions.

### Propose a new project

1. Open an issue with the
   [New project](https://github.com/CFA-Society-Mexico/propuestas/issues/new?template=proyecto-nuevo.yml)
   form in the [propuestas](https://github.com/CFA-Society-Mexico/propuestas) repository. If you prefer that your AI agent interviews you and fills it in, use the
   [proponer-proyecto](https://github.com/CFA-Society-Mexico/propuestas/blob/main/skills/proponer-proyecto/SKILL.md) skill.
2. The issue is public: do not include personal, contact, client or confidential information.
   Opening it does not imply acceptance, commitment or endorsement by CFA Society México or CFA
   Institute.
3. The maintainers reply in the issue within an estimated 1 to 2 weeks; it may take longer, since we
   review as volunteers. GitHub emails you.
4. Outcome: hosted in the organization (you get admin rights), listed on the profile from your
   account, changes requested, or closed with a short reason based on the criteria.

**Review criteria**

1. Relevant to the finance profession in Mexico, Latin America and other Spanish-speaking
   countries.
2. Meets the [minimum bar](#minimum-bar).
3. Contains no confidential data and discloses any commercial or employer relationship.
4. Has someone to maintain it.
5. Does not duplicate an existing project.

Ideas without a repository are reviewed with lower priority than projects in development or finished.

**If something sensitive was published by mistake**

1. Tell the maintainers in the same issue, without repeating the data, so they can delete it.
2. If the data remains in the edit history, GitHub Support is asked to purge it.
3. If it was a password, token or key, revoke it immediately: it is already considered compromised.

### Get listed on the profile

Only after your proposal is accepted:

1. Add the community contribution block shown in the Spanish section to your README.
2. Open a PR to this repository editing the "Proyectos / Projects" table in
   [`profile/README.md`](profile/README.md): one row with area, link, ES / EN description and author.
   Link the accepted issue in the PR.

### Code of conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
