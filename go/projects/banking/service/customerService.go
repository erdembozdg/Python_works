package service

import "github.com/erdembozdg/coding/go/projects/banking/domain"

type CustomerSerive interface {
	GetAllCustomer() ([]domain.Customer, error)
}

type DefaultCustomerService struct {
	repo domain.CutomerRepository
}

func (s DefaultCustomerService) GetAllCustomer() ([]domain.Customer, error) {
	return s.repo.FindAll()
}

func NewCustomerService(repository domain.CutomerRepository) DefaultCustomerService{
	return DefaultCustomerService{repo: repository}
}