// Fill out your copyright notice in the Description page of Project Settings.

#include "MyPlayerController_k3j9p2.h"

AMyPlayerController_k3j9p2::AMyPlayerController_k3j9p2()
{
	// Set this pawn to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
}

void AMyPlayerController_k3j9p2::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

	// Bind actions
	PlayerInputComponent->BindAction("Jump", IE_Pressed, this, &AMyPlayerController_k3j9p2::Jump);
	PlayerInputComponent->BindAction("Jump", IE_Released, this, &AMyPlayerController_k3j9p2::StopJumping);

	PlayerInputComponent->BindAxis("MoveForward", this, &AMyPlayerController_k3j9p2::MoveForward);
	PlayerInputComponent->BindAxis("MoveRight", this, &AMyPlayerController_k3j9p2::MoveRight);
}

void AMyPlayerController_k3j9p2::Jump()
{
	// Add jump functionality here
}

void AMyPlayerController_k3j9p2::StopJumping()
{
	// Add stop jumping functionality here
}

void AMyPlayerController_k3j9p2::MoveForward(float Value)
{
	// Add forward movement functionality here
}

void AMyPlayerController_k3j9p2::MoveRight(float Value)
{
	// Add right movement functionality here
}