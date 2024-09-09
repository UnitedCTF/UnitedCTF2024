package main

import (
	"bufio"
	"math/rand"
	"os"
	"time"
)

type FileReader struct {
    file   *os.File
    reader *bufio.Reader
    size   int64
    rng    *rand.Rand
}


func NewFileReader(filePath string) (*FileReader, error) {
    file, err := os.Open(filePath)
    if err != nil {
        return nil, err
    }

    fileInfo, err := file.Stat()
    if err != nil {
        file.Close()
        return nil, err
    }

    rng := rand.New(rand.NewSource(time.Now().UnixNano()))

    return &FileReader{
        file:   file,
        reader: bufio.NewReader(file),
        size:   fileInfo.Size(),
        rng:    rng,
    }, nil
}


func (r *FileReader) Close() error {
    return r.file.Close()
}


func (r *FileReader) RandomLine() (string, error) {
    randomPosition := r.rng.Int63n(r.size) - 20 // Step back 20 characters to avoid the last line

    _, err := r.file.Seek(randomPosition, 0)
    if err != nil {
        return "", err
    }

    r.reader.Reset(r.file)

    for {
        char, err := r.reader.ReadByte()
        if err != nil {
            return "", err
        }
        if char == '\n' {
            break
        }
    }

  line, err := r.reader.ReadString('\n')
    if err != nil {
        return "", err
    }

  return line[:len(line)-1], nil
}
