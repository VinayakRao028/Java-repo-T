package com.victorgarciarubio.ecommerce.entity;

import java.math.BigDecimal;
import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name="product")
@Getter
@Setter
@ApiModel(description = "Details about the product")
public class Product {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    @ApiModelProperty(notes = "The unique identifier of the product")
    private Long id;

    @ManyToOne
    @JoinColumn(name="category_id", nullable = false)
    @ApiModelProperty(notes = "The category of the product")
    private ProductCategory category;

    @Column(name = "sku")
    @ApiModelProperty(notes = "The stock keeping unit (SKU) of the product")
    private String sku;

    @Column(name = "name")
    @ApiModelProperty(notes = "The name of the product")
    private String name;

    @Column(name = "description")
    @ApiModelProperty(notes = "The description of the product")
    private String description;

    @Column(name = "unit_price")
    @ApiModelProperty(notes = "The unit price of the product")
    private BigDecimal unitPrice;

    @Column(name = "image_url")
    @ApiModelProperty(notes = "The URL of the product image")
    private String imageUrl;

    @Column(name = "active")
    @ApiModelProperty(notes = "Whether the product is active or not")
    private boolean active;

    @Column(name = "units_in_stock")
    @ApiModelProperty(notes = "The number of units in stock")
    private int unitsInStock;

    @Column(name = "date_created")
    @CreationTimestamp
    @ApiModelProperty(notes = "The date when the product was created")
    private Date dateCreated;

    @Column(name = "last_updated")
    @UpdateTimestamp
    @ApiModelProperty(notes = "The date when the product was last updated")
    private Date lastUpdated;
}