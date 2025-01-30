package com.victorgarciarubio.ecommerce.entity;

import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import lombok.Getter;
import lombok.Setter;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@Entity
@Table(name="product_category")
@Getter
@Setter
@ApiModel(description = "Details about the product category")
public class ProductCategory {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id")
    @ApiModelProperty(notes = "The unique identifier of the product category")
    private Long id;

    @Column(name="category_name")
    @ApiModelProperty(notes = "The name of the product category")
    private String categoryName;

    @OneToMany(cascade = CascadeType.ALL, mappedBy="category")
    @ApiModelProperty(notes = "The set of products belonging to this category")
    private Set<Product> products;
}