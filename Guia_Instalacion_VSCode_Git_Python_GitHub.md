<!-- Documento Markdown compuesto íntegramente con HTML y estilos inline. -->
<main style="box-sizing:border-box;max-width:1100px;margin:24px auto;padding:28px;background:#ffffff;color:#243447;font-family:Inter,'Segoe UI',Arial,sans-serif;font-size:17px;line-height:1.65;border:1px solid #d8e0e8;border-radius:18px;box-shadow:0 12px 35px rgba(11,61,110,.12);"><div style="box-sizing:border-box;overflow:hidden;margin:0 0 28px;padding:38px 30px;text-align:center;background:linear-gradient(135deg,#082f54 0%,#0b4f87 72%,#126aa8 100%);color:#ffffff;border-radius:14px;border-bottom:7px solid #d6a53a;">

<h1 id="guía-de-instalación-y-configuración" style="margin:0;color:#ffffff;font-size:clamp(30px,5vw,52px);line-height:1.12;">Guía de instalación y
configuración</h1>
<h2 id="vs-code--git--python--github" style="margin:14px 0 0;color:#eaf4ff;font-size:24px;line-height:1.25;border:0;padding:0;">VS Code · Git · Python ·
GitHub</h2>
<p style="display:inline-block;margin:20px 0 0;padding:9px 17px;background:#ffffff;color:#0b3d6e;border-radius:999px;font-size:16px;font-weight:700;"><strong>Laboratorio de Introducción a la Programación</strong><br>
<strong>Repositorio de trabajo:</strong> <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">Lab_IP</code></p>
</div>

<blockquote style="box-sizing:border-box;margin:16px 0;padding:14px 18px;background:#eef6ff;border:1px solid #b9d6f0;border-left:6px solid #0b4f87;border-radius:9px;">
<p style="margin:10px 0 14px;"><strong>Plataforma de referencia:</strong> Windows 10 u 11. Esta guía
utiliza las opciones predeterminadas de los instaladores y la casilla
<strong>Add python.exe to PATH</strong> disponible en Python para
Windows.</p>
</blockquote>
<section style="box-sizing:border-box;margin:0 0 28px;padding:20px 24px;background:#f7f9fb;border:1px solid #d8e0e8;border-left:6px solid #0b4f87;border-radius:12px;"><h2 id="índice" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">Índice</h2>
<ol type="1" style="margin:0;padding-left:24px;columns:2;column-gap:40px;">
<li style="margin:7px 0;"><a href="#1-resultado-esperado" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Resultado esperado</a></li>
<li style="margin:7px 0;"><a href="#2-enlaces-oficiales" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Enlaces oficiales</a></li>
<li style="margin:7px 0;"><a href="#3-instalar-vs-code-git-y-python" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Instalar VS Code, Git y
Python</a></li>
<li style="margin:7px 0;"><a href="#4-crear-una-cuenta-en-github" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Crear una cuenta en
GitHub</a></li>
<li style="margin:7px 0;"><a href="#5-crear-el-repositorio-lab_ip" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Crear el repositorio
Lab_IP</a></li>
<li style="margin:7px 0;"><a href="#6-clonar-el-repositorio-en-vs-code" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Clonar el repositorio
en VS Code</a></li>
<li style="margin:7px 0;"><a href="#7-crear-y-ejecutar-holamundopy" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Crear y ejecutar
holamundo.py</a></li>
<li style="margin:7px 0;"><a href="#8-realizar-el-primer-commit" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Realizar el primer
commit</a></li>
<li style="margin:7px 0;"><a href="#9-solucionar-el-error-de-identidad-de-git" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Solucionar el
error de identidad de Git</a></li>
<li style="margin:7px 0;"><a href="#10-sincronizar-y-comprobar-el-resultado" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Sincronizar y
comprobar el resultado</a></li>
</ol>
</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #d6a53a;border-radius:12px;"><h2 id="1-resultado-esperado" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">1. Resultado esperado</h2>
<p style="margin:10px 0 14px;">Al finalizar, se deberá contar con lo siguiente:</p>
<ul class="task-list">
<li style="margin:7px 0;"><label><input type="checkbox">Visual Studio Code
instalado.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">Git instalado.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">Python instalado y agregado a
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">PATH</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">La extensión oficial <strong>Python</strong> de Microsoft instalada en VS Code.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">Una cuenta activa en
GitHub.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">Un repositorio público llamado
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">Lab_IP</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El repositorio clonado y abierto en
VS Code.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">Un archivo llamado
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El archivo confirmado mediante un
commit y sincronizado con GitHub.</label></li>
</ul>
</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #0b4f87;border-radius:12px;"><h2 id="2-enlaces-oficiales" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">2. Enlaces oficiales</h2>
<div data-table-wrapper="true" style="margin:16px 0;overflow-x:auto;border-radius:9px;">
<table style="width:100%;border-collapse:collapse;background:#ffffff;border:1px solid #cfd8e3;">
<thead>
<tr class="header">
<th style="padding:12px 14px;text-align:left;vertical-align:top;background:#0b3d6e;color:#ffffff;border:1px solid #cfd8e3;">Herramienta o recurso</th>
<th style="padding:12px 14px;text-align:left;vertical-align:top;background:#0b3d6e;color:#ffffff;border:1px solid #cfd8e3;">Uso</th>
<th style="padding:12px 14px;text-align:left;vertical-align:top;background:#0b3d6e;color:#ffffff;border:1px solid #cfd8e3;">Enlaces</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Visual Studio Code</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">Editor de código</td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">
<a href="https://code.visualstudio.com/" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Sitio oficial</a> · <a href="https://code.visualstudio.com/Download" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Descargar VS Code</a>
</td>
</tr>
<tr class="even" style="background:#f7f9fb;">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Git</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">Control de versiones</td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">
<a href="https://git-scm.com/" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Sitio oficial</a> · <a href="https://git-scm.com/downloads" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Descargar Git</a> · <a href="https://git-scm.com/download/win" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Git for Windows</a>
</td>
</tr>
<tr class="odd">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Python</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">Lenguaje de programación</td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">
<a href="https://www.python.org/" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Sitio oficial</a> · <a href="https://www.python.org/downloads/" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Descargar Python</a> · <a href="https://www.python.org/downloads/windows/" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Python para
Windows</a> · <a href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Extensión Python para VS Code</a>
</td>
</tr>
<tr class="even" style="background:#f7f9fb;">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>GitHub</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">Alojamiento del repositorio</td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">
<a href="https://github.com/" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Abrir GitHub</a> · <a href="https://github.com/signup" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Crear una cuenta</a> · <a href="https://github.com/new" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Crear un repositorio</a>
</td>
</tr>
<tr class="odd">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>GNU GPL v3</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">Licencia del repositorio</td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Consultar la
licencia</a></td>
</tr>
<tr class="even" style="background:#f7f9fb;">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Solución del primer commit</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">Configuración de identidad de Git</td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><a href="https://github.com/unciafidelis/Python_workshop_2023/blob/main/01_Fundamentos/git.md" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Abrir
guía de referencia</a></td>
</tr>
</tbody>
</table>
</div>
<p style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:18px 0;">
  <a class="boton" href="https://code.visualstudio.com/Download" target="_blank" rel="noopener noreferrer" style="display:inline-block;margin:5px;padding:10px 15px;background:#0b4f87;color:#ffffff;text-decoration:none;font-weight:800;border-radius:8px;">⬇ Descargar VS Code</a>
  <a class="boton" href="https://git-scm.com/download/win" target="_blank" rel="noopener noreferrer" style="display:inline-block;margin:5px;padding:10px 15px;background:#0b4f87;color:#ffffff;text-decoration:none;font-weight:800;border-radius:8px;">⬇ Descargar Git</a>
  <a class="boton" href="https://www.python.org/downloads/windows/" target="_blank" rel="noopener noreferrer" style="display:inline-block;margin:5px;padding:10px 15px;background:#0b4f87;color:#ffffff;text-decoration:none;font-weight:800;border-radius:8px;">⬇ Descargar Python</a>
  <a class="boton" href="https://github.com/signup" target="_blank" rel="noopener noreferrer" style="display:inline-block;margin:5px;padding:10px 15px;background:#0b4f87;color:#ffffff;text-decoration:none;font-weight:800;border-radius:8px;">👤 Crear cuenta en GitHub</a>
</p>

<blockquote style="box-sizing:border-box;margin:16px 0;padding:14px 18px;background:#eef6ff;border:1px solid #b9d6f0;border-left:6px solid #0b4f87;border-radius:9px;">
<p style="margin:10px 0 14px;"><strong>Copiado rápido:</strong> los comandos y el código aparecen en
bloques independientes. En GitHub y en los visores Markdown compatibles
se pueden copiar mediante el ícono que aparece en la esquina superior
derecha de cada bloque.</p>
</blockquote>
</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #d6a53a;border-radius:12px;"><h2 id="3-instalar-vs-code-git-y-python" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">3. Instalar VS Code, Git y
Python</h2>
<h3 id="31-visual-studio-code" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">3.1 Visual Studio Code</h3>
<ol type="1">
<li style="margin:7px 0;">Abrir <a href="https://code.visualstudio.com/Download" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Descargar
Visual Studio Code</a>.</li>
<li style="margin:7px 0;">Descargar la versión para Windows.</li>
<li style="margin:7px 0;">Ejecutar el instalador.</li>
<li style="margin:7px 0;">Conservar todos los parámetros predeterminados.</li>
<li style="margin:7px 0;">Seleccionar <strong>Siguiente</strong> hasta que aparezca la opción
<strong>Instalar</strong>.</li>
<li style="margin:7px 0;">Finalizar la instalación.</li>
</ol>
<h3 id="32-git" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">3.2 Git</h3>
<ol type="1">
<li style="margin:7px 0;">Abrir <a href="https://git-scm.com/download/win" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Descargar Git for
Windows</a>.</li>
<li style="margin:7px 0;">Descargar y ejecutar el instalador.</li>
<li style="margin:7px 0;">Conservar todas las opciones predeterminadas.</li>
<li style="margin:7px 0;">Seleccionar <strong>Next/Siguiente</strong> en cada ventana, sin
modificar los parámetros.</li>
<li style="margin:7px 0;">Completar la instalación.</li>
</ol>
<h3 id="33-python" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">3.3 Python</h3>
<ol type="1">
<li style="margin:7px 0;"><p style="margin:10px 0 14px;">Abrir <a href="https://www.python.org/downloads/windows/" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Descargar Python para
Windows</a>.</p></li>
<li style="margin:7px 0;"><p style="margin:10px 0 14px;">Descargar la versión estable disponible para Windows.</p></li>
<li style="margin:7px 0;"><p style="margin:10px 0 14px;">Ejecutar el instalador.</p></li>
<li style="margin:7px 0;">
<p style="margin:10px 0 14px;">En la <strong>primera ventana</strong>, activar la casilla:</p>
<div style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-1',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="text" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code id="bloque-copiable-1" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;">Add python.exe to PATH</code></pre>
</div>
</li>
<li style="margin:7px 0;"><p style="margin:10px 0 14px;">Seleccionar <strong>Install Now</strong>.</p></li>
<li style="margin:7px 0;"><p style="margin:10px 0 14px;">Conservar el resto de las opciones predeterminadas y finalizar la
instalación.</p></li>
</ol>
<div class="alerta" style="box-sizing:border-box;margin:16px 0;padding:14px 18px;border-radius:9px;background:#fff8e1;border-left:6px solid #d6a53a;">

<p style="margin:10px 0 14px;"><strong>Importante:</strong> la casilla de <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">PATH</code> permite
ejecutar Python desde la terminal de VS Code. Si no se activa, el
comando <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">python</code> puede no ser reconocido.</p>
</div>

<h3 id="34-instalar-la-extension-python-en-vs-code" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">3.4 Instalar la extensión Python en VS Code</h3>
<ol type="1">
<li style="margin:7px 0;">Abrir <strong>Visual Studio Code</strong>.</li>
<li style="margin:7px 0;">Seleccionar el ícono de <strong>Extensions / Extensiones</strong> en la barra izquierda. El ícono está formado por varios cuadros apilados y normalmente se encuentra debajo de <strong>Source Control / Control de código fuente</strong>.</li>
<li style="margin:7px 0;">En el buscador de extensiones, escribir <strong>Python</strong>.</li>
<li style="margin:7px 0;">Seleccionar la extensión oficial <strong>Python</strong>, publicada por <strong>Microsoft</strong>, cuyo identificador es <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">ms-python.python</code>.</li>
<li style="margin:7px 0;">Seleccionar <strong>Install / Instalar</strong> y esperar a que finalice el proceso.</li>
</ol>
<p style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:18px 0;">
<a class="boton" href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" target="_blank" rel="noopener noreferrer" style="display:inline-block;margin:5px;padding:10px 15px;background:#0b4f87;color:#ffffff;text-decoration:none;font-weight:800;border-radius:8px;">Abrir extensión Python para VS Code</a>
</p>
<div class="exito" style="box-sizing:border-box;margin:16px 0;padding:14px 18px;border-radius:9px;background:#edf8ef;border-left:6px solid #23823d;">
<p style="margin:10px 0 14px;"><strong>Ejecución directa:</strong> después de instalar la extensión y abrir un archivo de Python, como <code style="padding:2px 6px;background:#ffffff;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code>, aparecerá el botón de reproducción <strong>▶ Run Python File / Ejecutar archivo Python</strong> en la parte superior derecha del editor. Seleccionarlo permite ejecutar el código directamente; el resultado se mostrará en la terminal integrada.</p>
</div>

<h3 id="35-comprobar-las-instalaciones" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">3.5 Comprobar las
instalaciones</h3>
<p style="margin:10px 0 14px;">Cerrar y volver a abrir VS Code después de instalar las herramientas.
Abrir la terminal desde <strong>Terminal → New Terminal/Nueva
terminal</strong> y ejecutar, uno por uno:</p>
<div class="sourceCode" id="cb2" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-2',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-2" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>code <span class="op">--</span>version</span></code></pre>
</div>
<div class="sourceCode" id="cb3" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-3',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-3" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>git <span class="op">--</span>version</span></code></pre>
</div>
<div class="sourceCode" id="cb4" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-4',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-4" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>python <span class="op">--</span>version</span></code></pre>
</div>
<p style="margin:10px 0 14px;">Si Windows no reconoce el último comando, comprobar también:</p>
<div class="sourceCode" id="cb5" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-5',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-5" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>py <span class="op">--</span>version</span></code></pre>
</div>
<p style="margin:10px 0 14px;">Cada comando debe mostrar un número de versión. Ejemplos:
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">git version 2.x.x</code> y <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">Python 3.x.x</code>.</p>
</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #0b4f87;border-radius:12px;"><h2 id="4-crear-una-cuenta-en-github" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">4. Crear una cuenta en GitHub</h2>
<ol type="1">
<li style="margin:7px 0;">Abrir <a href="https://github.com/signup" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Crear una cuenta en
GitHub</a>.</li>
<li style="margin:7px 0;">Registrar un correo electrónico accesible.</li>
<li style="margin:7px 0;">Crear una contraseña y un nombre de usuario.</li>
<li style="margin:7px 0;">Completar la verificación solicitada.</li>
<li style="margin:7px 0;">Confirmar el correo electrónico desde el mensaje enviado por
GitHub.</li>
<li style="margin:7px 0;">Iniciar sesión en <a href="https://github.com/login" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">GitHub</a>.</li>
</ol>
<blockquote style="box-sizing:border-box;margin:16px 0;padding:14px 18px;background:#eef6ff;border:1px solid #b9d6f0;border-left:6px solid #0b4f87;border-radius:9px;">
<p style="margin:10px 0 14px;">Se recomienda conservar el correo utilizado en GitHub, ya que se
necesitará para configurar la identidad de Git durante el primer
commit.</p>
</blockquote>
</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #d6a53a;border-radius:12px;"><h2 id="5-crear-el-repositorio-lab_ip" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">5. Crear el repositorio
Lab_IP</h2>
<p style="margin:10px 0 14px;">Abrir <a href="https://github.com/new" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Crear un repositorio nuevo</a>
y establecer <strong>exactamente</strong> estos parámetros:</p>
<div data-table-wrapper="true" style="margin:16px 0;overflow-x:auto;border-radius:9px;">
<table style="width:100%;border-collapse:collapse;background:#ffffff;border:1px solid #cfd8e3;">
<thead>
<tr class="header">
<th style="padding:12px 14px;text-align:left;vertical-align:top;background:#0b3d6e;color:#ffffff;border:1px solid #cfd8e3;">Parámetro</th>
<th style="padding:12px 14px;text-align:left;vertical-align:top;background:#0b3d6e;color:#ffffff;border:1px solid #cfd8e3;">Valor requerido</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Repository owner / Propietario</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">La cuenta personal del estudiante</td>
</tr>
<tr class="even" style="background:#f7f9fb;">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Repository name / Nombre</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">Lab_IP</code></td>
</tr>
<tr class="odd">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Description / Descripción</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;">Dejar en blanco</td>
</tr>
<tr class="even" style="background:#f7f9fb;">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Visibility / Visibilidad</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Public / Público</strong></td>
</tr>
<tr class="odd">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Repository template / Plantilla</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>No template / Sin plantilla</strong></td>
</tr>
<tr class="even" style="background:#f7f9fb;">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Add a README file</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Activado</strong></td>
</tr>
<tr class="odd">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Add .gitignore</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Python</strong></td>
</tr>
<tr class="even" style="background:#f7f9fb;">
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>Choose a license</strong></td>
<td style="padding:12px 14px;text-align:left;vertical-align:top;border:1px solid #cfd8e3;"><strong>GNU General Public License v3.0</strong></td>
</tr>
</tbody>
</table>
</div>
<p style="margin:10px 0 14px;">Después, seleccionar <strong>Create repository / Crear
repositorio</strong>.</p>
<div class="exito" style="box-sizing:border-box;margin:16px 0;padding:14px 18px;border-radius:9px;background:#edf8ef;border-left:6px solid #23823d;">

<p style="margin:10px 0 14px;">El repositorio correcto mostrará, como mínimo, los archivos
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">README.md</code>, <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">.gitignore</code> y
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">LICENSE</code>.</p>
</div>

</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #0b4f87;border-radius:12px;"><h2 id="6-clonar-el-repositorio-en-vs-code" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">6. Clonar el repositorio en
VS Code</h2>
<h3 id="61-comprobar-que-vs-code-detecta-git" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">6.1 Comprobar que VS Code
detecta Git</h3>
<ol type="1">
<li style="margin:7px 0;">Abrir VS Code.</li>
<li style="margin:7px 0;">Seleccionar <strong>Source Control / Control de código
fuente</strong> en la barra izquierda. Su ícono muestra tres círculos
conectados.</li>
<li style="margin:7px 0;">Deben aparecer las opciones:
<ul>
<li style="margin:7px 0;">
<strong>Open Folder / Abrir carpeta</strong>.</li>
<li style="margin:7px 0;">
<strong>Clone Repository / Clonar repositorio</strong>.</li>
</ul>
</li>
</ol>
<div class="error" style="box-sizing:border-box;margin:16px 0;padding:14px 18px;border-radius:9px;background:#ffeded;border-left:6px solid #b3261e;">

<p style="margin:10px 0 14px;">Si todavía aparece <strong>Install Git</strong>, <strong>Git for
Windows</strong> o una opción similar, cerrar VS Code por completo,
verificar que Git esté instalado y abrir VS Code nuevamente.</p>
</div>

<h3 id="62-autorizar-github" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">6.2 Autorizar GitHub</h3>
<ol type="1">
<li style="margin:7px 0;">Seleccionar <strong>Clone Repository / Clonar
repositorio</strong>.</li>
<li style="margin:7px 0;">Si VS Code solicita iniciar sesión, elegir <strong>Sign in with
GitHub / Iniciar sesión con GitHub</strong>.</li>
<li style="margin:7px 0;">El navegador se abrirá para solicitar autorización.</li>
<li style="margin:7px 0;">Aceptar el uso de GitHub desde Visual Studio Code mediante
<strong>Authorize Visual Studio Code</strong> o el botón
equivalente.</li>
<li style="margin:7px 0;">Regresar a VS Code cuando la autorización haya finalizado.</li>
</ol>
<h3 id="63-seleccionar-y-abrir-lab_ip" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">6.3 Seleccionar y abrir
Lab_IP</h3>
<ol type="1">
<li style="margin:7px 0;">Buscar y seleccionar el repositorio <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">Lab_IP</code>.</li>
<li style="margin:7px 0;">Elegir la carpeta donde se guardará la copia local. Puede ser:
<ul>
<li style="margin:7px 0;">Escritorio.</li>
<li style="margin:7px 0;">Documentos.</li>
<li style="margin:7px 0;">Una carpeta creada para la materia.</li>
<li style="margin:7px 0;">Cualquier ubicación con permisos de escritura.</li>
</ul>
</li>
<li style="margin:7px 0;">Esperar a que termine la clonación.</li>
<li style="margin:7px 0;">Seleccionar <strong>Open / Abrir</strong> para usar la misma ventana
o <strong>Open in New Window / Abrir en una ventana nueva</strong>.</li>
<li style="margin:7px 0;">Si VS Code pregunta si se confía en los autores de la carpeta,
confirmar únicamente si el repositorio corresponde a la cuenta
propia.</li>
</ol>
</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #d6a53a;border-radius:12px;"><h2 id="7-crear-y-ejecutar-holamundopy" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">7. Crear y ejecutar
holamundo.py</h2>
<h3 id="71-crear-el-archivo" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">7.1 Crear el archivo</h3>
<p style="margin:10px 0 14px;">En el explorador de VS Code:</p>
<ol type="1">
<li style="margin:7px 0;">Seleccionar <strong>New File / Nuevo archivo</strong>.</li>
<li style="margin:7px 0;">Escribir exactamente el nombre:</li>
</ol>
<div style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-6',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="text" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code id="bloque-copiable-6" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;">holamundo.py</code></pre>
</div>
<ol start="3" type="1">
<li style="margin:7px 0;">Dentro del archivo, escribir únicamente:</li>
</ol>
<div class="sourceCode" id="cb7" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-7',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode python" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode python" id="bloque-copiable-7" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a><span class="bu">print</span>(<span class="st">"hola mundo"</span>)</span></code></pre>
</div>
<ol start="4" type="1">
<li style="margin:7px 0;">Guardar con <kbd style="padding:3px 7px;background:#edf1f5;border:1px solid #b8c3cf;border-bottom-width:3px;border-radius:5px;font-family:inherit;">Ctrl</kbd> + <kbd style="padding:3px 7px;background:#edf1f5;border:1px solid #b8c3cf;border-bottom-width:3px;border-radius:5px;font-family:inherit;">S</kbd>.</li>
</ol>
<h3 id="72-ejecutar-la-prueba" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">7.2 Ejecutar la prueba</h3>
<p style="margin:10px 0 14px;">Abrir una terminal integrada en la carpeta del repositorio y
ejecutar:</p>
<div class="sourceCode" id="cb8" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-8',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-8" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>python holamundo<span class="op">.</span><span class="fu">py</span></span></code></pre>
</div>
<p style="margin:10px 0 14px;">Si el comando configurado en el equipo es <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">py</code>, usar:</p>
<div class="sourceCode" id="cb9" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-9',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-9" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb9-1"><a href="#cb9-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>py holamundo<span class="op">.</span><span class="fu">py</span></span></code></pre>
</div>
<p style="margin:10px 0 14px;">Resultado esperado:</p>
<div style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-10',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="text" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code id="bloque-copiable-10" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;">hola mundo</code></pre>
</div></section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #0b4f87;border-radius:12px;"><h2 id="8-realizar-el-primer-commit" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">8. Realizar el primer commit</h2>
<p style="margin:10px 0 14px;">Después de guardar <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code>, el ícono de
<strong>Source Control / Control de código fuente</strong> deberá
mostrar un pequeño círculo azul con el número <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">1</code>.</p>
<ol type="1">
<li style="margin:7px 0;">Seleccionar <strong>Source Control / Control de código
fuente</strong>.</li>
<li style="margin:7px 0;">En <strong>Changes / Cambios</strong>, localizar el archivo
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code>.</li>
<li style="margin:7px 0;">Seleccionar el ícono <strong>+</strong> para preparar el
cambio.</li>
</ol>
<blockquote style="box-sizing:border-box;margin:16px 0;padding:14px 18px;background:#eef6ff;border:1px solid #b9d6f0;border-left:6px solid #0b4f87;border-radius:9px;">
<p style="margin:10px 0 14px;">Si se selecciona el <strong>+</strong> situado junto al título
<strong>Changes / Cambios</strong>, se prepararán <strong>todos</strong>
los cambios del repositorio. En este ejercicio solamente debe existir
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code> como cambio nuevo.</p>
</blockquote>
<ol start="4" type="1">
<li style="margin:7px 0;">Comprobar que el archivo pase a <strong>Staged Changes / Cambios
preparados</strong>.</li>
<li style="margin:7px 0;">En la caja de mensaje situada sobre el botón
<strong>Commit</strong>, escribir exactamente:</li>
</ol>
<div style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-11',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="text" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code id="bloque-copiable-11" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;">CREATE holamundo.py</code></pre>
</div>
<ol start="6" type="1">
<li style="margin:7px 0;">Seleccionar <strong>Commit</strong>.</li>
</ol>
<p style="margin:10px 0 14px;">Es normal que en el primer intento aparezca un error si la identidad
de Git aún no ha sido configurada.</p>
</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #d6a53a;border-radius:12px;"><h2 id="9-solucionar-el-error-de-identidad-de-git" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">9. Solucionar el
error de identidad de Git</h2>
<p style="margin:10px 0 14px;">El error puede contener mensajes como los siguientes:</p>
<div style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-12',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="text" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code id="bloque-copiable-12" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;">Author identity unknown</code></pre>
</div>
<div style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-13',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="text" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code id="bloque-copiable-13" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;">Please tell me who you are.</code></pre>
</div>
<p style="margin:10px 0 14px;">La solución consiste en configurar el nombre y el correo que Git
registrará en los commits.</p>
<h3 id="91-configurar-el-nombre" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">9.1 Configurar el nombre</h3>
<p style="margin:10px 0 14px;">Abrir la terminal integrada de VS Code y copiar el siguiente comando.
Sustituir el texto entre comillas por el nombre real:</p>
<div class="sourceCode" id="cb14" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-14',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-14" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>git config <span class="op">--</span>global user<span class="op">.</span><span class="fu">name</span> <span class="st">"NOMBRE APELLIDO"</span></span></code></pre>
</div>
<p style="margin:10px 0 14px;">Ejemplo:</p>
<div class="sourceCode" id="cb15" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-15',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-15" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb15-1"><a href="#cb15-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>git config <span class="op">--</span>global user<span class="op">.</span><span class="fu">name</span> <span class="st">"Alejandro Morgan"</span></span></code></pre>
</div>
<h3 id="92-configurar-el-correo" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">9.2 Configurar el correo</h3>
<p style="margin:10px 0 14px;">Copiar el siguiente comando y sustituir el correo de ejemplo por el
correo utilizado en GitHub:</p>
<div class="sourceCode" id="cb16" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-16',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-16" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb16-1"><a href="#cb16-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>git config <span class="op">--</span>global user<span class="op">.</span><span class="fu">email</span> <span class="st">"correo@ejemplo.com"</span></span></code></pre>
</div>
<h3 id="93-verificar-la-configuración" style="margin:24px 0 9px;color:#15649a;font-size:23px;line-height:1.3;">9.3 Verificar la
configuración</h3>
<div class="sourceCode" id="cb17" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-17',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-17" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb17-1"><a href="#cb17-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>git config <span class="op">--</span>global user<span class="op">.</span><span class="fu">name</span></span></code></pre>
</div>
<div class="sourceCode" id="cb18" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-18',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode powershell" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode powershell" id="bloque-copiable-18" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb18-1"><a href="#cb18-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a>git config <span class="op">--</span>global user<span class="op">.</span><span class="fu">email</span></span></code></pre>
</div>
<p style="margin:10px 0 14px;">Los dos comandos deben mostrar los datos recién configurados.</p>
<p style="margin:10px 0 14px;">Para consultar la explicación original, abrir:</p>
<p style="margin:10px 0 14px;"><a href="https://github.com/unciafidelis/Python_workshop_2023/blob/main/01_Fundamentos/git.md" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;"><strong>Ver
solución de referencia en GitHub</strong></a></p>
<blockquote style="box-sizing:border-box;margin:16px 0;padding:14px 18px;background:#eef6ff;border:1px solid #b9d6f0;border-left:6px solid #0b4f87;border-radius:9px;">
<p style="margin:10px 0 14px;">El correo configurado puede quedar visible en el historial público de
commits. Si se desea mantenerlo privado, se puede utilizar el correo
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">noreply</code> proporcionado por GitHub en <a href="https://github.com/settings/emails" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">Settings → Emails</a>, siempre
que pertenezca a la cuenta.</p>
</blockquote>
</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #0b4f87;border-radius:12px;"><h2 id="10-sincronizar-y-comprobar-el-resultado" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">10. Sincronizar y
comprobar el resultado</h2>
<ol type="1">
<li style="margin:7px 0;">Regresar a <strong>Source Control / Control de código
fuente</strong>.</li>
<li style="margin:7px 0;">Seleccionar <strong>Commit</strong> nuevamente.</li>
<li style="margin:7px 0;">Cuando el commit finalice, seleccionar <strong>Sync Changes /
Sincronizar cambios</strong>.</li>
<li style="margin:7px 0;">Si aparece una confirmación para realizar <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">pull</code> y
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">push</code>, aceptarla.</li>
<li style="margin:7px 0;">Esperar a que finalice la sincronización.</li>
<li style="margin:7px 0;">Abrir <a href="https://github.com/" target="_blank" rel="noopener noreferrer" style="color:#0b5fa5;font-weight:700;text-decoration:none;">GitHub</a> en el navegador.</li>
<li style="margin:7px 0;">Entrar al repositorio <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">Lab_IP</code>.</li>
<li style="margin:7px 0;">Actualizar la página y comprobar que aparezca
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code>.</li>
<li style="margin:7px 0;">Abrir el archivo y verificar que contenga:</li>
</ol>
<div class="sourceCode" id="cb19" style="position:relative;margin:12px 0;">
<button type="button" onclick="copiarCodigo('bloque-copiable-19',this)" style="position:absolute;z-index:2;top:10px;right:10px;padding:7px 11px;background:#d6a53a;color:#1f2d3d;border:0;border-radius:6px;font-weight:800;cursor:pointer;">Copiar</button><pre class="sourceCode python" style="box-sizing:border-box;margin:0;padding:20px 95px 20px 20px;overflow:auto;background:#152536;color:#f4f7fa;border-radius:10px;border-left:5px solid #d6a53a;"><code class="sourceCode python" id="bloque-copiable-19" style="font-family:Consolas,'Courier New',monospace;color:#f4f7fa;background:transparent;"><span id="cb19-1"><a href="#cb19-1" aria-hidden="true" tabindex="-1" style="color:#0b5fa5;font-weight:700;text-decoration:none;"></a><span class="bu">print</span>(<span class="st">"hola mundo"</span>)</span></code></pre>
</div>
<div class="exito" style="box-sizing:border-box;margin:16px 0;padding:14px 18px;border-radius:9px;background:#edf8ef;border-left:6px solid #23823d;">

<p style="margin:10px 0 14px;"><strong>Práctica completada:</strong> el repositorio remoto
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">Lab_IP</code> contiene <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code> y el historial
muestra el commit <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">CREATE holamundo.py</code>.</p>
</div>

</section><section style="box-sizing:border-box;margin:28px 0;padding:24px;background:#ffffff;border:1px solid #d8e0e8;border-top:5px solid #d6a53a;border-radius:12px;"><h2 id="lista-final-de-comprobación" style="margin:0 0 16px;color:#0b3d6e;font-size:30px;line-height:1.25;border-bottom:1px solid #d8e0e8;padding-bottom:9px;">Lista final de comprobación</h2>
<ul class="task-list">
<li style="margin:7px 0;"><label><input type="checkbox">El repositorio se llama exactamente
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">Lab_IP</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El repositorio es
público.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El repositorio incluye
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">README.md</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El repositorio utiliza
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">.gitignore</code> para Python.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El repositorio incluye la licencia
GNU GPL v3.0.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">VS Code reconoce Git y muestra
<strong>Clone Repository</strong>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">La extensión oficial <strong>Python</strong> de Microsoft está instalada y el botón <strong>▶ Run Python File</strong> aparece al abrir <code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox"><code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">python --version</code> o
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">py --version</code> funciona en la terminal.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El archivo se llama exactamente
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El archivo contiene únicamente
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">print("hola mundo")</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox">El mensaje del commit es exactamente
<code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">CREATE holamundo.py</code>.</label></li>
<li style="margin:7px 0;"><label><input type="checkbox"><code style="padding:2px 6px;background:#edf1f5;color:#8b1e3f;border-radius:5px;font-family:Consolas,'Courier New',monospace;">holamundo.py</code> aparece en
GitHub después de sincronizar.</label></li>
</ul>
<p style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:18px 0;">
  <strong>Fin de la guía</strong><br>
  Laboratorio de Introducción a la Programación
</p>
</section></main>

<script>
function copiarCodigo(id, boton) {
  var elemento = document.getElementById(id);
  if (!elemento) return;
  var texto = elemento.innerText;
  function confirmar() {
    var original = boton.textContent;
    boton.textContent = 'Copiado';
    boton.style.background = '#23823d';
    boton.style.color = '#ffffff';
    window.setTimeout(function () {
      boton.textContent = original;
      boton.style.background = '#d6a53a';
      boton.style.color = '#1f2d3d';
    }, 1400);
  }
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(texto).then(confirmar);
    return;
  }
  var area = document.createElement('textarea');
  area.value = texto;
  area.style.position = 'fixed';
  area.style.opacity = '0';
  document.body.appendChild(area);
  area.select();
  document.execCommand('copy');
  document.body.removeChild(area);
  confirmar();
}
</script>
