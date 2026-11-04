# Dev Instructions

The user is in a live workshop: do what was asked and no more, answer questions in the chat, and don't test pages in a browser (i.e. no using `playwright` or similar).

## Dynamic Workflows

If asked to create dynamic workflows, keep them fairly short; they should also do what asked and no more.

## Building and Running the `app`

- The app is running in an isolated container.
- The frontend should access the backend on the same host, but different port, e.g.:
    ```
    const BASE_URL = `${window.location.protocol}//${window.location.host.replace(/(?<=[:-])[1-9][0-9][0-9][0-9]/,1002)}`
    ```
    - where the `app/docker-compose.yml` file defines which port the backend runs on
- The backend needs a CORS policy to allow the frontend to fetch the resources.
