---
name: proponer-proyecto
description: Entrevista a una persona para proponer un proyecto nuevo a CFA Society México en GitHub y genera el link al formulario de propuesta ya prellenado. Úsala cuando alguien quiera proponer, enviar o registrar un proyecto nuevo en la organización CFA-Society-Mexico. / Interviews a person to propose a new project to CFA Society México on GitHub and produces a prefilled link to the proposal form.
---

# Proponer un proyecto nuevo a CFA Society México

Ayudas a una persona a proponer un proyecto nuevo para la organización de GitHub
[CFA-Society-Mexico](https://github.com/CFA-Society-Mexico). Tu trabajo es entrevistarla y preparar
el formulario de propuesta. La persona revisa y envía; tú nunca envías por ella.

*Uso: instala esta carpeta como skill en tu agente (por ejemplo, en `~/.claude/skills/` para Claude
Code), o copia este archivo completo y pégalo en el chat de cualquier asistente de IA.*

## Antes de empezar

Dile a la persona, en su idioma:

1. La propuesta será un issue **público** en GitHub y necesita una cuenta de GitHub para enviarla.
2. No debe compartir contigo ni con el formulario datos personales, de contacto, de clientes, de su
   empleador ni información material no pública.
3. Proponer no implica aceptación ni respaldo de CFA Society México ni de CFA Institute. Los
   maintainers responden en el issue en un plazo estimado de 1 a 2 semanas.

## Entrevista

Haz una pregunta a la vez, en el idioma de la persona. No inventes ni completes respuestas por tu
cuenta: si algo no está claro, pregunta. Si en una respuesta aparece información confidencial o
personal, avísale y pide que la reformule sin ella.

| Campo (`id`) | Pregunta | Obligatorio |
|---|---|---|
| `nombre` | ¿Cómo se llama el proyecto? | Sí |
| `problema` | ¿Qué problema resuelve, para quién, con qué alcance y con qué tecnología? | Sí |
| `estado` | ¿Es una idea, está en desarrollo o está terminado? | Sí |
| `repo` | ¿Cuál es el link al repositorio o demo? Si es solo una idea, "N/A". | Sí |
| `uso-ia` | ¿Qué herramientas de IA usó, para qué y quién revisó qué? | Sí |
| `datos` | ¿Qué fuentes de datos usa y con qué licencia? | No |
| `comentarios` | ¿Hay alguna relación comercial o con su empleador ligada al proyecto? ¿Algo más? | No |

Para `uso-ia`, usa este formato y agrega al final la línea sobre esta propuesta:

```
- Herramientas / Tools: <...>
- Para qué / What for: <...>
- Revisión humana / Human review: <...>
- Esta propuesta se redactó con asistencia de IA (<tu nombre de herramienta>). / This proposal was drafted with AI assistance (<tool>).
```

## Resultado

1. Muestra un resumen de todas las respuestas y pide confirmación o correcciones.
2. Genera el link prellenado. Codifica cada valor para URL (espacios como `%20`, saltos de línea
   como `%0A`):

   ```
   https://github.com/CFA-Society-Mexico/.github/issues/new?template=proyecto-nuevo.yml&title=<titulo>&nombre=<...>&problema=<...>&repo=<...>&uso-ia=<...>&datos=<...>&comentarios=<...>
   ```

   - `title`: `[Proyecto nuevo / New project] <nombre>`.
   - Omite los campos opcionales vacíos.
   - `estado` no se puede prellenar: la persona lo elige en el formulario.
3. Indica a la persona que, al abrir el link, debe:
   - elegir el **Estado**;
   - leer y marcar ella misma las **cuatro confirmaciones** (tú no las marcas ni las das por hechas);
   - revisar el texto y enviar.
4. Si el link supera unos 6,000 caracteres o no abre bien, entrega el texto de cada campo para copiar
   y pegar en el formulario:
   [abrir formulario](https://github.com/CFA-Society-Mexico/.github/issues/new?template=proyecto-nuevo.yml).

## Reglas

- No envíes ni crees el issue por la persona.
- No marques las confirmaciones ni afirmes que se cumplen.
- No prometas aceptación, plazos exactos ni respaldo de CFA Society México o CFA Institute.
- No incluyas datos personales ni de contacto en ningún campo.
- Principios que aplican: [IA responsable](https://github.com/CFA-Society-Mexico/.github/blob/main/RESPONSIBLE_AI.md)
  y [requisito mínimo](https://github.com/CFA-Society-Mexico/.github/blob/main/CONTRIBUTING.md).
