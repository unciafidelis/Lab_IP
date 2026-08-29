<div align="center">

<img src="assets/guia-header.png" width="100%" alt="Guía de instalación y configuración de VS Code, Git, Python y GitHub">

[<img src="assets/buttons/vscode.png" width="250" alt="Descargar VS Code">](https://code.visualstudio.com/Download)
[<img src="assets/buttons/git.png" width="250" alt="Descargar Git">](https://git-scm.com/download/win)
[<img src="assets/buttons/python.png" width="250" alt="Descargar Python">](https://www.python.org/downloads/windows/)
[<img src="assets/buttons/github.png" width="250" alt="Crear cuenta en GitHub">](https://github.com/signup)

</div>

> [!NOTE]
> **Plataforma de referencia:** Windows 10 u 11. Esta guía utiliza las opciones predeterminadas de los instaladores y la casilla **Add python.exe to PATH** disponible en Python para Windows.

<a id="contenido"></a>

## <img src="assets/icons/contents.png" width="32" alt=""> Contenido

1. [Resultado esperado](#resultado-esperado)
2. [Enlaces oficiales](#enlaces-oficiales)
3. [Instalación de herramientas](#instalacion)
4. [Creación de la cuenta de GitHub](#cuenta-github)
5. [Creación del repositorio Lab_IP](#repositorio-lab-ip)
6. [Clonación del repositorio](#clonar-repositorio)
7. [Creación y ejecución de holamundo.py](#crear-ejecutar)
8. [Primer commit](#primer-commit)
9. [Solución del error de identidad](#identidad-git)
10. [Sincronización y comprobación](#sincronizar)

---

<a id="resultado-esperado"></a>

## <img src="assets/icons/result.png" width="32" alt=""> 1. Resultado esperado

Al finalizar, se deberá contar con lo siguiente:

- [ ] Visual Studio Code instalado.
- [ ] Git instalado.
- [ ] Python instalado y agregado a <code>PATH</code>.
- [ ] Extensión oficial **Python** de Microsoft instalada en VS Code.
- [ ] Cuenta activa en GitHub.
- [ ] Repositorio público llamado <code>Lab_IP</code>.
- [ ] Repositorio clonado y abierto en VS Code.
- [ ] Archivo llamado <code>holamundo.py</code>.
- [ ] Archivo confirmado mediante un commit y sincronizado con GitHub.

---

<a id="enlaces-oficiales"></a>

## <img src="assets/icons/links.png" width="32" alt=""> 2. Enlaces oficiales

| Herramienta o recurso | Uso | Enlaces |
|---|---|---|
| **Visual Studio Code** | Editor de código | [Sitio oficial](https://code.visualstudio.com/) · [Descargar VS Code](https://code.visualstudio.com/Download) |
| **Git** | Control de versiones | [Sitio oficial](https://git-scm.com/) · [Descargar Git](https://git-scm.com/downloads) · [Git for Windows](https://git-scm.com/download/win) |
| **Python** | Lenguaje de programación | [Sitio oficial](https://www.python.org/) · [Descargar Python](https://www.python.org/downloads/) · [Python para Windows](https://www.python.org/downloads/windows/) |
| **Extensión Python** | Ejecución de Python en VS Code | [Python de Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python) |
| **GitHub** | Alojamiento del repositorio | [Abrir GitHub](https://github.com/) · [Crear una cuenta](https://github.com/signup) · [Crear un repositorio](https://github.com/new) |
| **GNU GPL v3** | Licencia del repositorio | [Consultar la licencia](https://www.gnu.org/licenses/gpl-3.0.html) |
| **Solución del primer commit** | Configuración de identidad de Git | [Abrir guía de referencia](https://github.com/unciafidelis/Python_workshop_2023/blob/main/01_Fundamentos/git.md) |

> [!TIP]
> GitHub muestra automáticamente un botón de copiado en la esquina superior derecha de cada bloque de código.

---

<a id="instalacion"></a>

## <img src="assets/icons/install.png" width="32" alt=""> 3. Instalación de herramientas

### 3.1 Instalar Visual Studio Code

1. Abrir [Descargar Visual Studio Code](https://code.visualstudio.com/Download).
2. Descargar la versión para Windows.
3. Ejecutar el instalador.
4. Conservar todos los parámetros predeterminados.
5. Seleccionar **Siguiente** hasta que aparezca la opción **Instalar**.
6. Finalizar la instalación.

### 3.2 Instalar Git

1. Abrir [Descargar Git for Windows](https://git-scm.com/download/win).
2. Descargar y ejecutar el instalador.
3. Conservar todas las opciones predeterminadas.
4. Seleccionar **Next/Siguiente** en cada ventana.
5. No modificar parámetros ni elegir opciones diferentes de las predeterminadas.
6. Completar la instalación.

### 3.3 Instalar Python

1. Abrir [Descargar Python para Windows](https://www.python.org/downloads/windows/).
2. Descargar la versión estable disponible para Windows.
3. Ejecutar el instalador.
4. En la **primera ventana**, activar la siguiente casilla:

~~~text
Add python.exe to PATH
~~~

5. Seleccionar **Install Now**.
6. Conservar el resto de las opciones predeterminadas.
7. Finalizar la instalación.

> [!IMPORTANT]
> La casilla <code>PATH</code> permite ejecutar Python desde la terminal de VS Code. Si no se activa, el comando <code>python</code> puede no ser reconocido.

### <img src="assets/icons/extension.png" width="26" alt=""> 3.4 Instalar la extensión Python en VS Code

1. Abrir **Visual Studio Code**.
2. Seleccionar el ícono de **Extensions / Extensiones** en la barra izquierda.
   - El ícono está formado por varios cuadros apilados.
   - Normalmente se encuentra debajo de **Source Control / Control de código fuente**.
3. En el buscador de extensiones, escribir:

~~~text
Python
~~~

4. Seleccionar la extensión oficial **Python**, publicada por **Microsoft**.
5. Comprobar que su identificador sea:

~~~text
ms-python.python
~~~

6. Seleccionar **Install / Instalar**.
7. Esperar a que finalice la instalación.

[<img src="assets/buttons/extension.png" width="270" alt="Instalar extensión Python para VS Code">](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

> [!TIP]
> Después de instalar la extensión y abrir un archivo de Python, como <code>holamundo.py</code>, aparecerá el botón **▶ Run Python File / Ejecutar archivo Python** en la parte superior derecha del editor. Al seleccionarlo, el código se ejecutará y el resultado aparecerá en la terminal integrada.

### 3.5 Comprobar las instalaciones

Cerrar y volver a abrir VS Code después de instalar las herramientas. Abrir la terminal desde **Terminal → New Terminal/Nueva terminal** y ejecutar, uno por uno:

~~~powershell
code --version
~~~

~~~powershell
git --version
~~~

~~~powershell
python --version
~~~

Si Windows no reconoce el último comando, comprobar también:

~~~powershell
py --version
~~~

Cada comando debe mostrar un número de versión. Por ejemplo:

~~~text
git version 2.x.x
Python 3.x.x
~~~

---

<a id="cuenta-github"></a>

## <img src="assets/icons/account.png" width="32" alt=""> 4. Crear una cuenta en GitHub

1. Abrir [Crear una cuenta en GitHub](https://github.com/signup).
2. Registrar un correo electrónico accesible.
3. Crear una contraseña y un nombre de usuario.
4. Completar la verificación solicitada.
5. Confirmar el correo electrónico desde el mensaje enviado por GitHub.
6. Iniciar sesión en [GitHub](https://github.com/login).

> [!NOTE]
> Se recomienda conservar el correo utilizado en GitHub, ya que se necesitará para configurar la identidad de Git durante el primer commit.

---

<a id="repositorio-lab-ip"></a>

## <img src="assets/icons/repository.png" width="32" alt=""> 5. Crear el repositorio Lab_IP

Abrir [Crear un repositorio nuevo](https://github.com/new) y establecer **exactamente** estos parámetros:

| Parámetro | Valor requerido |
|---|---|
| **Repository owner / Propietario** | Cuenta personal del estudiante |
| **Repository name / Nombre** | <code>Lab_IP</code> |
| **Description / Descripción** | Dejar en blanco |
| **Visibility / Visibilidad** | **Public / Público** |
| **Repository template / Plantilla** | **No template / Sin plantilla** |
| **Add a README file** | **Activado** |
| **Add .gitignore** | **Python** |
| **Choose a license** | **GNU General Public License v3.0** |

Después, seleccionar **Create repository / Crear repositorio**.

> [!TIP]
> El repositorio correcto mostrará, como mínimo, los archivos <code>README.md</code>, <code>.gitignore</code> y <code>LICENSE</code>.

---

<a id="clonar-repositorio"></a>

## <img src="assets/icons/clone.png" width="32" alt=""> 6. Clonar el repositorio en VS Code

### 6.1 Comprobar que VS Code detecta Git

1. Abrir VS Code.
2. Seleccionar **Source Control / Control de código fuente** en la barra izquierda.
   - Su ícono muestra tres círculos conectados.
3. Comprobar que aparezcan las siguientes opciones:
   - **Open Folder / Abrir carpeta**.
   - **Clone Repository / Clonar repositorio**.

> [!WARNING]
> Si todavía aparece **Install Git**, **Git for Windows** o una opción similar, cerrar VS Code por completo, verificar que Git esté instalado y abrir VS Code nuevamente.

### 6.2 Autorizar GitHub

1. Seleccionar **Clone Repository / Clonar repositorio**.
2. Si VS Code solicita iniciar sesión, elegir **Sign in with GitHub / Iniciar sesión con GitHub**.
3. El navegador se abrirá para solicitar autorización.
4. Aceptar el uso de GitHub desde VS Code mediante **Authorize Visual Studio Code** o el botón equivalente.
5. Regresar a VS Code cuando finalice la autorización.

### 6.3 Seleccionar y abrir Lab_IP

1. Buscar y seleccionar el repositorio <code>Lab_IP</code>.
2. Elegir la carpeta donde se guardará la copia local. Puede ser:
   - Escritorio.
   - Documentos.
   - Una carpeta creada para la materia.
   - Cualquier ubicación con permisos de escritura.
3. Esperar a que termine la clonación.
4. Seleccionar **Open / Abrir** para usar la misma ventana o **Open in New Window / Abrir en una ventana nueva**.
5. Si VS Code pregunta si se confía en los autores de la carpeta, confirmar únicamente si el repositorio corresponde a la cuenta propia.

---

<a id="crear-ejecutar"></a>

## <img src="assets/icons/python.png" width="32" alt=""> 7. Crear y ejecutar holamundo.py

### 7.1 Crear el archivo

1. En el explorador de VS Code, seleccionar **New File / Nuevo archivo**.
2. Escribir exactamente el nombre:

~~~text
holamundo.py
~~~

3. Dentro del archivo, escribir únicamente:

~~~python
print("hola mundo")
~~~

4. Guardar con <kbd>Ctrl</kbd> + <kbd>S</kbd>.

### <img src="assets/icons/play.png" width="26" alt=""> 7.2 Ejecutar mediante el botón Play

1. Abrir <code>holamundo.py</code> en VS Code.
2. Localizar el botón **▶ Run Python File / Ejecutar archivo Python** en la parte superior derecha.
3. Seleccionar el botón **▶**.
4. Revisar el resultado en la terminal integrada.

> [!NOTE]
> Si VS Code solicita elegir un intérprete, seleccionar la versión de Python instalada en el equipo.

### 7.3 Ejecutar desde la terminal

Abrir una terminal integrada en la carpeta del repositorio y ejecutar:

~~~powershell
python holamundo.py
~~~

Si el comando configurado en el equipo es <code>py</code>, utilizar:

~~~powershell
py holamundo.py
~~~

Resultado esperado:

~~~text
hola mundo
~~~

---

<a id="primer-commit"></a>

## <img src="assets/icons/commit.png" width="32" alt=""> 8. Realizar el primer commit

Después de guardar <code>holamundo.py</code>, el ícono de **Source Control / Control de código fuente** deberá mostrar un pequeño círculo azul con el número <code>1</code>.

1. Seleccionar **Source Control / Control de código fuente**.
2. En **Changes / Cambios**, localizar el archivo <code>holamundo.py</code>.
3. Seleccionar el ícono **+** para preparar el cambio.
4. Comprobar que el archivo pase a **Staged Changes / Cambios preparados**.
5. En la caja situada sobre el botón **Commit**, escribir exactamente:

~~~text
CREATE holamundo.py
~~~

6. Seleccionar **Commit**.

> [!NOTE]
> Si se selecciona el ícono **+** situado junto al título **Changes / Cambios**, se prepararán todos los cambios del repositorio. En este ejercicio solamente debe existir <code>holamundo.py</code> como cambio nuevo.

> [!IMPORTANT]
> Es normal que en el primer intento aparezca un error si la identidad de Git todavía no ha sido configurada.

---

<a id="identidad-git"></a>

## <img src="assets/icons/identity.png" width="32" alt=""> 9. Solucionar el error de identidad de Git

El error puede incluir alguno de estos mensajes:

~~~text
Author identity unknown
~~~

~~~text
Please tell me who you are.
~~~

La solución consiste en configurar el nombre y el correo que Git registrará en los commits.

### 9.1 Configurar el nombre

Abrir la terminal integrada de VS Code, copiar el siguiente comando y sustituir el texto entre comillas por el nombre real:

~~~powershell
git config --global user.name "NOMBRE APELLIDO"
~~~

Ejemplo:

~~~powershell
git config --global user.name "Alejandro Morgan"
~~~

### 9.2 Configurar el correo

Copiar el siguiente comando y sustituir el correo de ejemplo por el correo utilizado en GitHub:

~~~powershell
git config --global user.email "correo@ejemplo.com"
~~~

### 9.3 Verificar la configuración

~~~powershell
git config --global user.name
~~~

~~~powershell
git config --global user.email
~~~

Los dos comandos deben mostrar los datos recién configurados.

[**Consultar la solución de referencia en GitHub**](https://github.com/unciafidelis/Python_workshop_2023/blob/main/01_Fundamentos/git.md)

> [!CAUTION]
> El correo configurado puede quedar visible en el historial público de commits. Para mantenerlo privado se puede utilizar el correo <code>noreply</code> proporcionado por GitHub en [Settings → Emails](https://github.com/settings/emails), siempre que pertenezca a la cuenta.

---

<a id="sincronizar"></a>

## <img src="assets/icons/upload.png" width="32" alt=""> 10. Sincronizar y comprobar el resultado

1. Regresar a **Source Control / Control de código fuente**.
2. Seleccionar **Commit** nuevamente.
3. Cuando el commit finalice, seleccionar **Sync Changes / Sincronizar cambios**.
4. Si aparece una confirmación para realizar <code>pull</code> y <code>push</code>, aceptarla.
5. Esperar a que finalice la sincronización.
6. Abrir [GitHub](https://github.com/) en el navegador.
7. Entrar al repositorio <code>Lab_IP</code>.
8. Actualizar la página y comprobar que aparezca <code>holamundo.py</code>.
9. Abrir el archivo y verificar que contenga:

~~~python
print("hola mundo")
~~~

> [!TIP]
> **Práctica completada:** el repositorio remoto <code>Lab_IP</code> contiene <code>holamundo.py</code> y el historial muestra el commit <code>CREATE holamundo.py</code>.

---

<a id="lista-final"></a>

## <img src="assets/icons/final-check.png" width="32" alt=""> Lista final de comprobación

- [ ] El repositorio se llama exactamente <code>Lab_IP</code>.
- [ ] El repositorio es público.
- [ ] El repositorio incluye <code>README.md</code>.
- [ ] El repositorio utiliza <code>.gitignore</code> para Python.
- [ ] El repositorio incluye la licencia GNU GPL v3.0.
- [ ] VS Code reconoce Git y muestra **Clone Repository**.
- [ ] La extensión oficial **Python** de Microsoft está instalada.
- [ ] El botón **▶ Run Python File** aparece al abrir <code>holamundo.py</code>.
- [ ] <code>python --version</code> o <code>py --version</code> funciona en la terminal.
- [ ] El archivo se llama exactamente <code>holamundo.py</code>.
- [ ] El archivo contiene únicamente <code>print("hola mundo")</code>.
- [ ] El mensaje del commit es exactamente <code>CREATE holamundo.py</code>.
- [ ] <code>holamundo.py</code> aparece en GitHub después de sincronizar.

---

<div align="center">

**Fin de la guía**

Laboratorio de Introducción a la Programación

</div>
