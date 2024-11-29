# Resumen Completo sobre Celdas y Paneles Fotovoltaicos  

## Celdas Fotovoltaicas  
Las celdas fotovoltaicas convierten la luz en electricidad mediante el **efecto fotoeléctrico**, donde los fotones liberan electrones en ciertos materiales. El **silicio cristalino** es el material más utilizado por varias razones:  
- **Abundancia y costo:** El silicio es el segundo elemento más abundante en la Tierra, lo que lo hace relativamente económico.  
- **Propiedades semiconductoras:** El silicio tiene una banda prohibida de aproximadamente 1.1 eV, lo que lo hace ideal para absorber luz visible.  
- **Durabilidad y estabilidad:** Su forma cristalina permite una mejor estructura para el transporte de electrones, aumentando la eficiencia y la vida útil de las celdas.  

Las celdas suelen ser de tipo **monocristalino** o **policristalino**:  
- **Monocristalino:** Ofrece mayor eficiencia debido a la uniformidad en la estructura del cristal, pero es más caro de producir.  
- **Policristalino:** Es menos eficiente pero más económico, ya que se fabrica con múltiples cristales en una misma celda.  

Los paneles solares están formados por varias celdas conectadas en serie y en paralelo para optimizar la generación de energía.

## Modelo Eléctrico de la Celda  
El comportamiento eléctrico se modela con la **ecuación del diodo**:  

![image](https://github.com/user-attachments/assets/9caefe99-7674-44ad-bf5e-565c56484854)

**Donde:**  
- `I`: Corriente de salida.  
- `I_L`: Corriente generada por la luz.  
- `I_0`: Corriente de saturación inversa.  
- `q`: Carga del electrón.  
- `V`: Voltaje de la celda.  
- `n`: Factor de idealidad.  
- `k`: Constante de Boltzmann.  
- `T`: Temperatura de la celda.  

La eficiencia de la celda disminuye con el aumento de la temperatura porque afecta tanto la corriente como el voltaje, lo que reduce la potencia generada (![image](https://github.com/user-attachments/assets/d027bd56-86b1-44d3-8530-1813f3c9a61b)).  

---

## Transferencia de Calor en Paneles Fotovoltaicos  
La energía térmica se disipa mediante tres mecanismos: **conducción**, **convección** y **radiación**.  

### 1. Conducción  
Proceso en el que el calor fluye dentro de un material sólido debido a la interacción entre partículas. Se describe mediante la **Ley de Fourier**:  

![image](https://github.com/user-attachments/assets/5e307ebb-57b0-404c-953a-9bdb2a533de4) 

**Donde:**  
- `k`: Conductividad térmica.  
- `∇T`: Gradiente de temperatura.  

En el contexto de paneles solares, la conducción se da principalmente en las capas internas del panel, como el vidrio y el encapsulante.  

### 2. Convección  
Ocurre en líquidos o gases y depende del movimiento de masas de fluido. La **ley de enfriamiento de Newton** la describe:  

![image](https://github.com/user-attachments/assets/1de882f2-4884-40ba-9b29-b4c24446149c)  

**Donde:**  
- `h`: Coeficiente de convección.  
- `ΔT`: Diferencia de temperatura entre el cuerpo y el ambiente.  

En paneles solares, la convección ocurre en el aire que rodea al panel.  

### 3. Radiación  
Es la energía emitida por un cuerpo en forma de ondas electromagnéticas. Se modela con la **Ley de Stefan-Boltzmann**:  

![image](https://github.com/user-attachments/assets/1a76364d-679b-4556-b04c-1f0be619f8db)  

**Donde:**  
- `ε`: Emisividad del material.  
- `σ`: Constante de Stefan-Boltzmann.  
- `T_s`: Temperatura de la superficie.  
- `T_∞`: Temperatura ambiente.  

La radiación es especialmente relevante en condiciones de alta exposición solar, donde el panel debe disipar el calor para evitar pérdidas de eficiencia.  

---

## Disipadores de Calor  
Los disipadores ayudan a mantener la temperatura de los paneles solares bajo control y pueden ser:  
- **Activos:** Utilizan energía externa (bombas o ventiladores) para enfriar.  
- **Pasivos:** Usan **aletas** para aumentar la superficie de contacto con el aire y disipar el calor de manera natural.  

Los disipadores pasivos son más comunes en paneles solares debido a su bajo costo y facilidad de mantenimiento.  

---
z
---
z
---
z
---
z
---
z
---
z
---

## Modelo Matemático y Ecuación Diferencial  
El comportamiento térmico en las aletas de los disipadores se modela con una **ecuación diferencial de segundo orden** basada en el balance energético:  

![image](https://github.com/user-attachments/assets/c347e3e2-4e92-4fd4-9ae4-3a869862500a)  

Esta ecuación considera los efectos combinados de conducción, convección y radiación, permitiendo predecir la distribución de temperatura y optimizar el diseño de los disipadores.  

---

## Puntos Clave para Exponer  
- Explica qué es el efecto fotoeléctrico y la importancia del silicio cristalino en las celdas solares.  
- Destaca la ecuación del diodo y cómo la temperatura afecta la eficiencia.  
- Describe los tres mecanismos de transferencia de calor y da ejemplos.  
- Explica los tipos de disipadores de calor y sus ventajas.  
- Concluye con el modelo matemático para el balance térmico y su importancia en el diseño de aletas.  
