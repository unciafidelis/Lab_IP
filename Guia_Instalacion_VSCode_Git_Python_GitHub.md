<style>
:root {
  --azul: #0d47a1;
  --azul-claro: #eaf2ff;
  --verde: #1b5e20;
  --verde-claro: #edf7ed;
  --dorado: #c69214;
  --gris: #455a64;
  --gris-claro: #f5f7f9;
  --rojo: #b71c1c;
  --borde: #d7dee5;
}

body {
  color: #1f2933;
  font-family: Inter, "Segoe UI", Arial, sans-serif;
  font-size: 17px;
  line-height: 1.65;
  margin: 0 auto;
  max-width: 1050px;
  padding: 24px;
}

h1, h2, h3 {
  color: var(--azul);
  line-height: 1.25;
}

h1 {
  border-bottom: 4px solid var(--dorado);
  padding-bottom: 12px;
}

h2 {
  border-bottom: 1px solid var(--borde);
  margin-top: 38px;
  padding-bottom: 8px;
}

table {
  border-collapse: collapse;
  margin: 18px 0;
  width: 100%;
}

th {
  background: var(--azul);
  color: #ffffff;
}

th, td {
  border: 1px solid var(--borde);
  padding: 11px 14px;
  text-align: left;
  vertical-align: top;
}

tr:nth-child(even) {
  background: var(--gris-claro);
}

blockquote {
  background: var(--azul-claro);
  border-left: 5px solid var(--azul);
  margin: 18px 0;
  padding: 12px 18px;
}

code {
  background: #eef1f4;
  border-radius: 5px;
  color: #8b1e3f;
  padding: 2px 6px;
}

pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}

.boton {
  background: var(--azul);
  border-radius: 7px;
  color: #ffffff !important;
  display: inline-block;
  font-weight: 700;
  margin: 4px 6px 4px 0;
  padding: 8px 13px;
  text-decoration: none;
}

.exito {
  background: var(--verde-claro);
  border-left: 5px solid var(--verde);
  padding: 12px 18px;
}

.alerta {
  background: #fff8e1;
  border-left: 5px solid var(--dorado);
  padding: 12px 18px;
}

.error {
  background: #ffebee;
  border-left: 5px solid var(--rojo);
  padding: 12px 18px;
}
</style>

<div align="center">

# Guía de instalación y configuración

## VS Code · Git · Python · GitHub

**Laboratorio de Introducción a la Programación**  
**Repositorio de trabajo:** `Lab_IP`

</div>

> **Plataforma de referencia:** Windows 10 u 11. Esta guía utiliza las opciones predeterminadas de los instaladores y la casilla **Add python.exe to PATH** disponible en Python para Windows.

## Índice

1. [Resultado esperado](#1-resultado-esperado)
2. [Enlaces oficiales](#2-enlaces-oficiales)
3. [Instalar VS Code, Git y Python](#3-instalar-vs-code-git-y-python)
4. [Crear una cuenta en GitHub](#4-crear-una-cuenta-en-github)
5. [Crear el repositorio Lab_IP](#5-crear-el-repositorio-lab_ip)
6. [Clonar el repositorio en VS Code](#6-clonar-el-repositorio-en-vs-code)
7. [Crear y ejecutar holamundo.py](#7-crear-y-ejecutar-holamundopy)
8. [Realizar el primer commit](#8-realizar-el-primer-commit)
9. [Solucionar el error de identidad de Git](#9-solucionar-el-error-de-identidad-de-git)
10. [Sincronizar y comprobar el resultado](#10-sincronizar-y-comprobar-el-resultado)

---

## 1. Resultado esperado

Al finalizar, se deberá contar con lo siguiente:

- [ ] Visual Studio Code instalado.
- [ ] Git instalado.
- [ ] Python instalado y agregado a `PATH`.
- [ ] Una cuenta activa en GitHub.
- [ ] Un repositorio público llamado `Lab_IP`.
- [ ] El repositorio clonado y abierto en VS Code.
- [ ] Un archivo llamado `holamundo.py`.
- [ ] El archivo confirmado mediante un commit y sincronizado con GitHub.

---

## 2. Enlaces oficiales

| Herramienta o recurso | Uso | Enlaces |
|---|---|---|
| **Visual Studio Code** | Editor de código | [Sitio oficial](https://code.visualstudio.com/) · [Descargar VS Code](https://code.visualstudio.com/Download) |
| **Git** | Control de versiones | [Sitio oficial](https://git-scm.com/) · [Descargar Git](https://git-scm.com/downloads) · [Git for Windows](https://git-scm.com/download/win) |
| **Python** | Lenguaje de programación | [Sitio oficial](https://www.python.org/) · [Descargar Python](https://www.python.org/downloads/) · [Python para Windows](https://www.python.org/downloads/windows/) |
| **GitHub** | Alojamiento del repositorio | [Abrir GitHub](https://github.com/) · [Crear una cuenta](https://github.com/signup) · [Crear un repositorio](https://github.com/new) |
| **GNU GPL v3** | Licencia del repositorio | [Consultar la licencia](https://www.gnu.org/licenses/gpl-3.0.html) |
| **Solución del primer commit** | Configuración de identidad de Git | [Abrir guía de referencia](https://github.com/unciafidelis/Python_workshop_2023/blob/main/01_Fundamentos/git.md) |

<p align="center">
  <a class="boton" href="https://code.visualstudio.com/Download">⬇ Descargar VS Code</a>
  <a class="boton" href="https://git-scm.com/download/win">⬇ Descargar Git</a>
  <a class="boton" href="https://www.python.org/downloads/windows/">⬇ Descargar Python</a>
  <a class="boton" href="https://github.com/signup">👤 Crear cuenta en GitHub</a>
</p>

> **Copiado rápido:** los comandos y el código aparecen en bloques independientes. En GitHub y en los visores Markdown compatibles se pueden copiar mediante el ícono que aparece en la esquina superior derecha de cada bloque.

---

## 3. Instalar VS Code, Git y Python

### 3.1 Visual Studio Code

1. Abrir [Descargar Visual Studio Code](https://code.visualstudio.com/Download).
2. Descargar la versión para Windows.
3. Ejecutar el instalador.
4. Conservar todos los parámetros predeterminados.
5. Seleccionar **Siguiente** hasta que aparezca la opción **Instalar**.
6. Finalizar la instalación.

### 3.2 Git

1. Abrir [Descargar Git for Windows](https://git-scm.com/download/win).
2. Descargar y ejecutar el instalador.
3. Conservar todas las opciones predeterminadas.
4. Seleccionar **Next/Siguiente** en cada ventana, sin modificar los parámetros.
5. Completar la instalación.

### 3.3 Python

1. Abrir [Descargar Python para Windows](https://www.python.org/downloads/windows/).
2. Descargar la versión estable disponible para Windows.
3. Ejecutar el instalador.
4. En la **primera ventana**, activar la casilla:

   ```text
   Add python.exe to PATH
   ```

5. Seleccionar **Install Now**.
6. Conservar el resto de las opciones predeterminadas y finalizar la instalación.

<div class="alerta">

**Importante:** la casilla de `PATH` permite ejecutar Python desde la terminal de VS Code. Si no se activa, el comando `python` puede no ser reconocido.

</div>

### 3.4 Comprobar las instalaciones

Cerrar y volver a abrir VS Code después de instalar las herramientas. Abrir la terminal desde **Terminal → New Terminal/Nueva terminal** y ejecutar, uno por uno:

```powershell
code --version
```

```powershell
git --version
```

```powershell
python --version
```

Si Windows no reconoce el último comando, comprobar también:

```powershell
py --version
```

Cada comando debe mostrar un número de versión. Ejemplos: `git version 2.x.x` y `Python 3.x.x`.

---

## 4. Crear una cuenta en GitHub

1. Abrir [Crear una cuenta en GitHub](https://github.com/signup).
2. Registrar un correo electrónico accesible.
3. Crear una contraseña y un nombre de usuario.
4. Completar la verificación solicitada.
5. Confirmar el correo electrónico desde el mensaje enviado por GitHub.
6. Iniciar sesión en [GitHub](https://github.com/login).

> Se recomienda conservar el correo utilizado en GitHub, ya que se necesitará para configurar la identidad de Git durante el primer commit.

---

## 5. Crear el repositorio Lab_IP

Abrir [Crear un repositorio nuevo](https://github.com/new) y establecer **exactamente** estos parámetros:

| Parámetro | Valor requerido |
|---|---|
| **Repository owner / Propietario** | La cuenta personal del estudiante |
| **Repository name / Nombre** | `Lab_IP` |
| **Description / Descripción** | Dejar en blanco |
| **Visibility / Visibilidad** | **Public / Público** |
| **Repository template / Plantilla** | **No template / Sin plantilla** |
| **Add a README file** | **Activado** |
| **Add .gitignore** | **Python** |
| **Choose a license** | **GNU General Public License v3.0** |

Después, seleccionar **Create repository / Crear repositorio**.

<div class="exito">

El repositorio correcto mostrará, como mínimo, los archivos `README.md`, `.gitignore` y `LICENSE`.

</div>

---

## 6. Clonar el repositorio en VS Code

### 6.1 Comprobar que VS Code detecta Git

1. Abrir VS Code.
2. Seleccionar **Source Control / Control de código fuente** en la barra izquierda. Su ícono muestra tres círculos conectados.
3. Deben aparecer las opciones:
   - **Open Folder / Abrir carpeta**.
   - **Clone Repository / Clonar repositorio**.

<div class="error">

Si todavía aparece **Install Git**, **Git for Windows** o una opción similar, cerrar VS Code por completo, verificar que Git esté instalado y abrir VS Code nuevamente.

</div>

### 6.2 Autorizar GitHub

1. Seleccionar **Clone Repository / Clonar repositorio**.
2. Si VS Code solicita iniciar sesión, elegir **Sign in with GitHub / Iniciar sesión con GitHub**.
3. El navegador se abrirá para solicitar autorización.
4. Aceptar el uso de GitHub desde Visual Studio Code mediante **Authorize Visual Studio Code** o el botón equivalente.
5. Regresar a VS Code cuando la autorización haya finalizado.

### 6.3 Seleccionar y abrir Lab_IP

1. Buscar y seleccionar el repositorio `Lab_IP`.
2. Elegir la carpeta donde se guardará la copia local. Puede ser:
   - Escritorio.
   - Documentos.
   - Una carpeta creada para la materia.
   - Cualquier ubicación con permisos de escritura.
3. Esperar a que termine la clonación.
4. Seleccionar **Open / Abrir** para usar la misma ventana o **Open in New Window / Abrir en una ventana nueva**.
5. Si VS Code pregunta si se confía en los autores de la carpeta, confirmar únicamente si el repositorio corresponde a la cuenta propia.

---

## 7. Crear y ejecutar holamundo.py

### 7.1 Crear el archivo

En el explorador de VS Code:

1. Seleccionar **New File / Nuevo archivo**.
2. Escribir exactamente el nombre:

```text
holamundo.py
```

3. Dentro del archivo, escribir únicamente:

```python
print("hola mundo")
```

4. Guardar con <kbd>Ctrl</kbd> + <kbd>S</kbd>.

### 7.2 Ejecutar la prueba

Abrir una terminal integrada en la carpeta del repositorio y ejecutar:

```powershell
python holamundo.py
```

Si el comando configurado en el equipo es `py`, usar:

```powershell
py holamundo.py
```

Resultado esperado:

```text
hola mundo
```

---

## 8. Realizar el primer commit

Después de guardar `holamundo.py`, el ícono de **Source Control / Control de código fuente** deberá mostrar un pequeño círculo azul con el número `1`.

1. Seleccionar **Source Control / Control de código fuente**.
2. En **Changes / Cambios**, localizar el archivo `holamundo.py`.
3. Seleccionar el ícono **+** para preparar el cambio.

> Si se selecciona el **+** situado junto al título **Changes / Cambios**, se prepararán **todos** los cambios del repositorio. En este ejercicio solamente debe existir `holamundo.py` como cambio nuevo.

4. Comprobar que el archivo pase a **Staged Changes / Cambios preparados**.
5. En la caja de mensaje situada sobre el botón **Commit**, escribir exactamente:

```text
CREATE holamundo.py
```

6. Seleccionar **Commit**.

Es normal que en el primer intento aparezca un error si la identidad de Git aún no ha sido configurada.

---

## 9. Solucionar el error de identidad de Git

El error puede contener mensajes como los siguientes:

```text
Author identity unknown
```

```text
Please tell me who you are.
```

La solución consiste en configurar el nombre y el correo que Git registrará en los commits.

### 9.1 Configurar el nombre

Abrir la terminal integrada de VS Code y copiar el siguiente comando. Sustituir el texto entre comillas por el nombre real:

```powershell
git config --global user.name "NOMBRE APELLIDO"
```

Ejemplo:

```powershell
git config --global user.name "Alejandro Morgan"
```

### 9.2 Configurar el correo

Copiar el siguiente comando y sustituir el correo de ejemplo por el correo utilizado en GitHub:

```powershell
git config --global user.email "correo@ejemplo.com"
```

### 9.3 Verificar la configuración

```powershell
git config --global user.name
```

```powershell
git config --global user.email
```

Los dos comandos deben mostrar los datos recién configurados.

Para consultar la explicación original, abrir:

[**Ver solución de referencia en GitHub**](https://github.com/unciafidelis/Python_workshop_2023/blob/main/01_Fundamentos/git.md)

> El correo configurado puede quedar visible en el historial público de commits. Si se desea mantenerlo privado, se puede utilizar el correo `noreply` proporcionado por GitHub en [Settings → Emails](https://github.com/settings/emails), siempre que pertenezca a la cuenta.

---

## 10. Sincronizar y comprobar el resultado

1. Regresar a **Source Control / Control de código fuente**.
2. Seleccionar **Commit** nuevamente.
3. Cuando el commit finalice, seleccionar **Sync Changes / Sincronizar cambios**.
4. Si aparece una confirmación para realizar `pull` y `push`, aceptarla.
5. Esperar a que finalice la sincronización.
6. Abrir [GitHub](https://github.com/) en el navegador.
7. Entrar al repositorio `Lab_IP`.
8. Actualizar la página y comprobar que aparezca `holamundo.py`.
9. Abrir el archivo y verificar que contenga:

```python
print("hola mundo")
```

<div class="exito">

**Práctica completada:** el repositorio remoto `Lab_IP` contiene `holamundo.py` y el historial muestra el commit `CREATE holamundo.py`.

</div>

---

## Lista final de comprobación

- [ ] El repositorio se llama exactamente `Lab_IP`.
- [ ] El repositorio es público.
- [ ] El repositorio incluye `README.md`.
- [ ] El repositorio utiliza `.gitignore` para Python.
- [ ] El repositorio incluye la licencia GNU GPL v3.0.
- [ ] VS Code reconoce Git y muestra **Clone Repository**.
- [ ] `python --version` o `py --version` funciona en la terminal.
- [ ] El archivo se llama exactamente `holamundo.py`.
- [ ] El archivo contiene únicamente `print("hola mundo")`.
- [ ] El mensaje del commit es exactamente `CREATE holamundo.py`.
- [ ] `holamundo.py` aparece en GitHub después de sincronizar.

---

<p align="center">
  <strong>Fin de la guía</strong><br>
  Laboratorio de Introducción a la Programación
</p>
