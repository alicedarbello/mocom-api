---
name: Default Task Issue
about: Use this template to get an idea of what should include a Task Issue
title: 'Feat/Fix: Implementar...'
labels: task
assignees: ''

---

## Contexto

Necesitamos [desarrollar/ajustar] la funcionalidad de... para permitir que el usuario...

Relacionado con: **Epic #[Numero]**

---

## Especificaciones Técnicas

* **Endpoint:** `[GET/POST] /api/v...`
* **Acceso:** `[Público / Requiere Auth / Requiere Admin]`
* **Tabla/Modelo DB:** `[NombreTabla]`

---

## Input (Request)

```json
{
  "campo": "tipo_dato",
  "ejemplo": "valor"
}
```

---

## Output (Response)

### Caso de Éxito

```json
{
  "resultado": "ok"
}
```

### Casos de Error

* **Error 4xx:** Mensaje esperado...
* **Estado Vacío:** Si no hay datos, mostrar...

---

## Criterios de Aceptación (Definition of Done)

* [ ] La funcionalidad cumple con las especificaciones técnicas.
* [ ] Se han manejado los casos de error descritos.
* [ ] El endpoint devuelve los códigos de estado HTTP correctos.
* [ ] El código pasa el linter y no rompe tests existentes.

---

## Notas de Implementación

* Investigar librería X para...
* Recordar no exponer datos sensibles en el log...
