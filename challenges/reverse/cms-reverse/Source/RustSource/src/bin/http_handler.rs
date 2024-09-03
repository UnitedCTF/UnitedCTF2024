use std::collections::HashMap;

pub struct HTTP_Handler {
    http_server_url: String,
}
impl HTTP_Handler {
    pub fn new(http_server_url: String,port:String) -> HTTP_Handler {
        HTTP_Handler { http_server_url: format!("http://{}:{}", http_server_url, port) }
    }
    pub async fn do_get_request(&self, endpoint: &'static str) -> Result<String, String> {
        let url = &format!("{}/{}", self.http_server_url, endpoint);
        match reqwest::get(url).await {
            Ok(response) => Ok(response.text().await.unwrap()),
            Err(err) => Err(format!(
                "The get request to {} returned status code {}",
                url,
                err.status().unwrap().to_string()
            )
            .to_string()),
        }
    }

    pub async fn do_post_request(
        &self,
        endpoint: &'static str,
        body: &[(String, String)],
    ) -> Result<String, String> {
        let url = &format!("{}/{}", self.http_server_url, endpoint);
        let client = reqwest::Client::new();
        match client.post(url).form(body).send().await {
            Ok(response) => Ok(response.text().await.unwrap()),
            Err(err) => Err(format!(
                "The post request to {} returned status code {}",
                url,
                err.status().unwrap().to_string()
            )
            .to_string()),
        }
    }
}
