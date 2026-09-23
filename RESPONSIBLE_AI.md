# IA responsable / Responsible AI

Principios comunitarios de CFA Society México para herramientas financieras construidas con IA o
para usarse con IA. Se inspiran en el
[Código de Ética y Estándares de Conducta Profesional de CFA Institute](https://www.cfainstitute.org/standards/professionals/code-ethics-standards),
pero no son una interpretación oficial de CFA Institute ni lo sustituyen.

*Community principles of CFA Society México for financial tools built with or for AI. English
version [below](#english).*

## Español

### 1. Responsabilidad humana

**Qué significa.** La IA asiste; la persona que usa la herramienta es responsable de la conclusión,
recomendación o reporte que resulte.

**Por qué.** Estándar V(A), Diligencia y base razonable: toda recomendación necesita una base
razonable y adecuada, respaldada por investigación apropiada. Un resultado de IA sin revisar no es
una base razonable.

- **Haz:** revisa y valida cada fórmula, cifra y conclusión generada con IA antes de publicarla.
- **No hagas:** presentar el resultado de un modelo como conclusión final sin revisión humana.

### 2. Transparencia

**Qué significa.** Cada herramienta documenta sus supuestos, fuentes de datos y limitaciones.

**Por qué.** Estándar V(B), Comunicación con clientes y potenciales clientes: divulgar el proceso,
los riesgos y las limitaciones, y distinguir entre hechos y opiniones.

- **Haz:** incluye en el README una sección de supuestos y limitaciones (por ejemplo, "asume
  volatilidad constante" o "datos con rezago de 15 minutos").
- **No hagas:** esconder supuestos en el código ni usar datos cuyo origen no puedas citar.

### 3. Confidencialidad

**Qué significa.** Nunca datos de clientes, información confidencial ni información material no
pública en prompts, código, ejemplos, tests o historial de git.

**Por qué.** Estándar III(E), Preservación de la confidencialidad, y Estándar II(A), Información
material no pública.

- **Haz:** usa datos públicos o sintéticos, y revisa que tus prompts de ejemplo no contengan
  información de tu empleador.
- **No hagas:** pegar reportes internos, posiciones de portafolio ni datos personales en una
  herramienta de IA o en un repositorio público. Si ocurre, avisa a los maintainers de inmediato:
  borrar un archivo no lo elimina del historial de git.

### 4. No es asesoría de inversión

**Qué significa.** Las herramientas son de apoyo educativo y analítico. No consideran la situación,
los objetivos ni las restricciones de ningún inversionista.

**Por qué.** Estándar III(C), Idoneidad, y Estándar I(C), Tergiversación: los resultados no deben
presentarse como garantizados ni como recomendaciones personalizadas.

- **Haz:** incluye un aviso visible en el README y, si aplica, en la interfaz.
- **No hagas:** usar lenguaje como "compra ya", "rendimiento garantizado" o "señal segura".

### 5. Divulgación del uso de IA

**Qué significa.** Cada repositorio indica dónde y cómo se usó IA para construirlo, y quién lo
revisó.

**Por qué.** Estándar I(C), Tergiversación: no presentar como propio, ni como verificado, un trabajo
que no lo es.

- **Haz:** agrega una sección "Uso de IA" al README con el formato de
  [CONTRIBUTING.md](CONTRIBUTING.md).
- **No hagas:** omitir el uso de IA porque "solo fue para el boilerplate".

## English

### 1. Human accountability

**What it means.** AI assists; the person using the tool owns the resulting conclusion,
recommendation or report.

**Why.** Standard V(A), Diligence and Reasonable Basis: every recommendation needs a reasonable and
adequate basis, supported by appropriate research. Unreviewed AI output is not a reasonable basis.

- **Do:** review and validate every AI-generated formula, figure and conclusion before publishing.
- **Don't:** present a model's output as a final conclusion without human review.

### 2. Transparency

**What it means.** Every tool documents its assumptions, data sources and limitations.

**Why.** Standard V(B), Communication with Clients and Prospective Clients: disclose the process,
risks and limitations, and distinguish fact from opinion.

- **Do:** include an assumptions-and-limitations section in the README (for example, "assumes
  constant volatility" or "data delayed 15 minutes").
- **Don't:** hide assumptions in code or use data whose origin you cannot cite.

### 3. Confidentiality

**What it means.** Never client data, confidential information or material non-public information
in prompts, code, examples, tests or git history.

**Why.** Standard III(E), Preservation of Confidentiality, and Standard II(A), Material Nonpublic
Information.

- **Do:** use public or synthetic data, and check that your example prompts contain nothing from
  your employer.
- **Don't:** paste internal reports, portfolio positions or personal data into an AI tool or a
  public repository. If it happens, tell the maintainers immediately: deleting a file does not
  remove it from git history.

### 4. Not investment advice

**What it means.** Tools are educational and analytical aids. They do not consider any investor's
situation, objectives or constraints.

**Why.** Standard III(C), Suitability, and Standard I(C), Misrepresentation: results must not be
presented as guaranteed or as personalized recommendations.

- **Do:** include a visible disclaimer in the README and, where relevant, in the interface.
- **Don't:** use language like "buy now", "guaranteed return" or "sure signal".

### 5. Disclosure of AI use

**What it means.** Every repository states where and how AI was used to build it, and who reviewed
it.

**Why.** Standard I(C), Misrepresentation: do not present work as your own, or as verified, when it
is not.

- **Do:** add an "AI use" section to the README using the format in
  [CONTRIBUTING.md](CONTRIBUTING.md).
- **Don't:** skip disclosure because "it was only boilerplate".
