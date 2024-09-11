use sha2::{Digest, Sha256};

pub fn compare_hash(plain:&String, hash:&String) -> bool{
    let mut hasher = Sha256::new();
    hasher.update(plain.as_bytes());
    let result = hasher.finalize();
    let result_str = format!("{:x}",result);
    result_str == hash.clone()
}