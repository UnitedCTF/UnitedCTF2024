import torch
from typing import List

from const import FLAG, MODEL_PATH


class AiModel:
    def __init__(self, flag: str):
        self.model = torch.nn.Sequential()
        for i in range(len(flag)):
            self.model.add_module(f"layer{i}", torch.nn.Linear(1, 1))

        print(f"Model created with {len(flag)} layers")
        self.change_weights([*flag])
        print("Weights changed")

    def change_weights(self, weights: List[str]):
        for i, param in enumerate(self.model.parameters()):
            # Flag is stored in the weights and not in the biases
            if param.data.ndimension() != 2:  # Weight
                continue

            weight_value = float(f"0.{ord(weights[i // 2])}")
            param.data = torch.tensor([[weight_value]])

    def save_weights(self, path: str):
        """Save model weights to a file"""
        torch.save(self.model, path)
        print(f"Model saved to {path}")

    def solve(self, path: str) -> str:
        # Load the model
        self.model = torch.load(path, weights_only=False)
        print(f"Model loaded from {path}")

        flag = ""
        for param in self.model.parameters():

            # Flag is stored in the weights and not in the biases
            if param.data.ndimension() != 2:
                continue
            weight = param.data[0].item()
            # 1. Multiply by 1000 to get the ASCII value
            value = weight * 1000
            # 2. Round the value to the nearest integer
            value = round(value)
            # 3. Convert the integer to ASCII character
            if value < 127:
                value = chr(int(value))
            else:
                # Value is greater than 127 which means it was a letter bellow 100, divide by 10 and convert to ASCII
                value = chr(int(value / 10))
            flag += value

        print("Flag:", flag)
        return flag


if __name__ == "__main__":
    model = AiModel(FLAG)
    model.save_weights(MODEL_PATH)

    solved_flag: str = model.solve(MODEL_PATH)

    assert FLAG == solved_flag
    print("Flag is correct!")
