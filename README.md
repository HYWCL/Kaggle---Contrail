<div align="center">
<h2> Kaggle - Google Research Identify Contrails to Reduce Global Warming </h2>
</div>

![237503761-b0930ea9-f0b3-4243-8eeb-bf0f6435f310](https://github.com/HYWCL/Kaggle---Contrail/assets/86766552/2fc0ec87-bbc1-4a4c-9f13-40192fa76dcb)

콘트레일(비행운)은 항공기 엔진 배기구에서 형성되는 얼음 결정 구름으로, 대기 중 열을 가둬 지구 온난화에 영향을 끼칠 수 있습니다. <br> 연구자들은 콘트레일이 언제 형성될지와 그로 인한 온난화 정도를 예측하는 모델을 개발했지만 검증이 필요합니다. <br> 귀하의 작업은 이러한 콘트레일 모델의 정확성을 높이는 데 도움이 될 것입니다. 이를 통해 항공사들은 콘트레일 생성을 줄이고 기후 변화에 미치는 영향을 감소시킬 수 있습니다.

## 대회 설명
<img src="https://github.com/HYWCL/Kaggle---Contrail/assets/86766552/25484a71-9268-4024-a82e-fb197fd6d085" width="250" height="250"/>
<img src="https://github.com/HYWCL/Kaggle---Contrail/assets/86766552/94d8cf71-a5c5-4187-9cdf-f5d8bd224077" width="250" height="250"/>
<img src="https://github.com/HYWCL/Kaggle---Contrail/assets/86766552/1902d658-0bf6-4b33-9f70-9757f2c1a694" width="250" height="250"/>

왼쪽부터 순서대로 False Color Image, Ground Truth Contrail Mask, Contrail Mask on False Color Image 입니다.

## 코드 설명
 - contrail-unet-train.ipynb (Pytorch - Unet을 이용한 훈련)
 - contrail-unet2-infer.ipynb (Pytorch - Unet을 이용한 추론)
 - contrails-dataset-ash-color.ipynb (데이터 전처리)
 - gr-icrgw-training-with-4-folds.ipynb (PytorchLightning - Unet을 이용한 훈련)
 - gr-icrgw-inference-4-folds.ipynb (PytorchLightning - Unet을 이용한 추론)

## 대회 결과
![1](https://github.com/HYWCL/Kaggle---Contrail/assets/86766552/61c4edb7-58b3-40ba-b444-635a735e816b)
