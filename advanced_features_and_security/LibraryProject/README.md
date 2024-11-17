# Permissions and Groups in Bookshelf

## Groups
1. **Editors**: Can create and edit books.
2. **Viewers**: Can view books only.
3. **Admins**: Have full access to all actions.

## Permissions
The following permissions are defined for the `Book` model:
- `can_view`: View books.
- `can_create`: Add new books.
- `can_edit`: Modify existing books.
- `can_delete`: Remove books.

## Testing
1. Assign users to groups in the Django admin panel.
2. Use the following URLs to test:
   - `/books/` - View book list.
   - `/books/add/` - Add a new book (Editors only).
   - `/books/edit/<pk>/` - Edit an existing book (Editors only).

## Note
Make sure to run `python manage.py setup_groups` to initialize groups and permissions programmatically.
