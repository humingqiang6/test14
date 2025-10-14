#include "MyGameCharacter.h"
#include "Camera/CameraComponent.h"
#include "GameFramework/SpringArmComponent.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "Engine/Engine.h"

// Sets default values
AMyGameCharacter::AMyGameCharacter()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	// Create the camera boom
	SpringArm = CreateDefaultSubobject<USpringArmComponent>(TEXT("CameraBoom"));
	SpringArm->SetupAttachment(RootComponent);
	SpringArm->bUsePawnControlRotation = true; // Rotate the arm based on the controller

	// Create the camera
	Camera = CreateDefaultSubobject<UCameraComponent>(TEXT("Camera"));
	Camera->SetupAttachment(SpringArm, USpringArmComponent::SocketName);
	Camera->bUsePawnControlRotation = false; // Use the SpringArm rotation instead

	// Configure character movement
	GetCharacterMovement()->bOrientRotationToMovement = true; // Rotate character to match movement direction
	GetCharacterMovement()->RotationRate = FRotator(0.0f, 600.0f, 0.0f); // Set rotation rate
}

// Called when the game starts or when spawned
void AMyGameCharacter::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AMyGameCharacter::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

// Called to bind functionality to input
void AMyGameCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

	// Bind axis mappings
	PlayerInputComponent->BindAxis("MoveForward", this, &AMyGameCharacter::MoveForward);
	PlayerInputComponent->BindAxis("MoveRight", this, &AMyGameCharacter::MoveRight);
	PlayerInputComponent->BindAxis("LookUp", this, &AMyGameCharacter::LookUp);
	PlayerInputComponent->BindAxis("Turn", this, &AMyGameCharacter::Turn);
}

// Input functions
void AMyGameCharacter::MoveForward(float Value)
{
	if (Value != 0.0f)
	{
		AddMovementInput(GetActorForwardVector(), Value);
	}
}

void AMyGameCharacter::MoveRight(float Value)
{
	if (Value != 0.0f)
	{
		AddMovementInput(GetActorRightVector(), Value);
	}
}

void AMyGameCharacter::LookUp(float Value)
{
	if (Value != 0.0f)
	{
		AddControllerPitchInput(Value);
	}
}

void AMyGameCharacter::Turn(float Value)
{
	if (Value != 0.0f)
	{
		AddControllerYawInput(Value);
	}
}