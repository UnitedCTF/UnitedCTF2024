use const_format::formatcp;

const PORT:u32 = 10000;
const HTTP_SERVER_URL:&'static str = formatcp!("http://ctf.unitedctf.ca:{}",PORT);

pub async fn do_get_request(endpoint:&'static str) -> Result<String,String>{
    let url = &format!("{}/{}",HTTP_SERVER_URL,endpoint);
    match reqwest::get(url).await {
        Ok(response) => Ok(response.text().await.unwrap()),
        Err(err) => Err(format!("The get request to {} returned status code {}",url,err.status().unwrap().to_string()).to_string())
    }
}

pub async fn do_post_request(endpoint:&'static str,body:&[(String,String)]) -> Result<String,String>{
    let url = &format!("{}/{}",HTTP_SERVER_URL,endpoint);
    let client = reqwest::Client::new();
    match client.post(url).form(body).send().await {
        Ok(response) => Ok(response.text().await.unwrap()),
        Err(err) => Err(format!("The post request to {} returned status code {}",url,err.status().unwrap().to_string()).to_string())
    }
}