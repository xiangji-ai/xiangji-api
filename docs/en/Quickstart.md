# Quickstart

The Piclaza API provides a simple interface for image/video processing.

## API Keys

The Piclaza API uses API keys to authenticate requests. You can view your API keys in the Piclaza [Account Page](https://www.piclaza.com/console/user/account).

> ℹ️ Please note:
> 
> API Keys are credentials used for authentication and billing, please keep them secure! Do not share your API Keys with others or expose them in client-side code (browsers, apps).
>
> If your API Key becomes compromised, you can contact us for help.
> 

## Authentication


All API requests require your API Key in the HTTP header.

```
X-API-Key: [YOUR_API_KEY]
```

All API requests must be made over HTTPS. Calls made over plain HTTP will fail.
